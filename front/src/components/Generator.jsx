import './generator.css'
import {useEffect, useState} from "react";
import axios from "axios";

export default () => {
    // TODO: заменить
    const [typeOptions, setTypeOptions] = useState([])
    const [selectedType, setSelectedType] = useState("INN")
    const [selectedSubType, setSelectedSubType] = useState("")
    const [quantity, setQuantity] = useState(1)
    const [generationResult, setGenerationResult] = useState([])
    const [errorMessage, setErrorMessage] = useState("")

    useEffect(() => {
        getTypeOptions()
            .then(options => setTypeOptions(options))
    }, [])


    const getTypeOptions = async () => {
        const { data } = await axios.get("/generate/types")
        return data
    }

    const getSubTypesOptionEls = () => {
        const selectedTypeOption = typeOptions.find(o => o.name === selectedType)

        if (selectedTypeOption !== undefined) {
            return (
                <div className="col">
                    <label className="label" htmlFor="subType">
                        Подтип:
                    </label>
                    <select id="subType"
                            value={selectedSubType}
                            onChange={e => setSelectedSubType(e.target.value)}>
                        <option disabled value={""} key={"disabled"}> -- Выберите подтип -- </option>
                        {selectedTypeOption.subTypes.map(opt => (
                            <option key={opt.name} value={opt.name}>{opt.label}</option>
                        ))}
                    </select>
                </div>
            )
        }
    }

    const submitGenerateForm = async event => {
        event.preventDefault()

        if (!selectedType || !selectedSubType || !quantity) {
            setErrorMessage("Необходимо заполнить все поля")
            return
        }

        const { data } = await axios.post("/generate", {
            "type": selectedType,
            "sub_type": selectedSubType,
            "quantity": quantity
        })

        setGenerationResult(data)
        setSelectedType("INN")
        setSelectedSubType("")
        setQuantity(1)
        setErrorMessage("")
    }

    return (
        <div className="generator">
            <form className="form" onSubmit={submitGenerateForm}>
                <div className="col">
                    <label className="label" htmlFor="type">
                        Тип:
                    </label>
                    <select id="type"
                            value={selectedType}
                            onChange={e => setSelectedType(e.target.value)}>
                        <option disabled value={""} key={"disabled"}> -- Выберите тип -- </option>
                        {typeOptions.map(opt => (
                            <option key={opt.name} value={opt.name}>{opt.label}</option>
                        ))}
                    </select>
                </div>

                {getSubTypesOptionEls()}

                <div className="col">
                    <label className="label" htmlFor="quantity">
                        Кол-во генерируемых сущностей:
                    </label>
                    <input className="quantity"
                           id="quantity"
                           value={quantity}
                           onChange={e => setQuantity(parseInt(e.target.value))}
                    />
                </div>

                <div className="col">
                    <button type="submit">Сгенерировать</button>
                </div>
            </form>

            <div className="error-message">{errorMessage}</div>

            <div className="generator-result">
                <ul>
                    {generationResult.map(value => (
                        <li key={value}>{value}</li>
                    ))}
                </ul>
            </div>
        </div>
    )
}