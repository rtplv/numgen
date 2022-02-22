import './generator.css'
import {useState} from "react";

const getTypeOptions = () => {
    const options = ["ИНН", "СНИЛС"]
    const optionsEls = [
        <option key="disabled" disabled>Выберите тип</option>
    ]

    for (const opt of options) {
        optionsEls.push(<option key={opt} value={opt}>{opt}</option>)
    }

    return optionsEls
}


export default () => {
    // TODO: заменить
    const [type, setType] = useState("ИНН")
    const [count, setCount] = useState(0)

    const submitGenerateForm = event => {
        event.preventDefault()
        // TODO: заменить
        setType("ИНН")
        setCount(0)
    }


    return (
        <div className="generator">
            <form className="form" onSubmit={submitGenerateForm}>
                <div className="col">
                    <label className="label" htmlFor="type">
                        Тип:
                    </label>
                    <select id="type"
                            value={type}
                            onChange={e => setType(e.target.value)}>
                        {getTypeOptions()}
                    </select>
                </div>

                <div className="col">
                    <label className="label" htmlFor="count">
                        Кол-во генерируемых сущностей:
                    </label>
                    <input className="count"
                           id="count"
                           value={count}
                           onChange={e => setCount(parseInt(e.target.value))}
                    />
                </div>

                <div className="col">
                    <button type="submit">Сгенерировать</button>
                </div>
            </form>
        </div>
    )
}