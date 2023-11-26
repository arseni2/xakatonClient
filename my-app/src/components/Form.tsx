const Form = () => {
    // const [borrower, setBorrower] = useState<string>('')
    //
    // const [coBorrower, setCoBorrower] = useState<string>()
    // const [guarantor, setGuarantor] = useState<string>()
    //
    // const [bankProduct, setBankProduct] = useState<string>()
    // const [maxSum, setMaxSum] = useState<string>()
    // const [maxTime, setTime] = useState<string>()
    // const [productOffer, setProductOffer] = useState<string>()
    // const [monthPay, setMonthPay] = useState<string>()
    //
    // const [passport, setPassport] = useState<FileList | null>(null)
    // const [moneyData, setMoneyData] = useState<FileList | null>()
    // const [otherDoc, setOtherDoc] = useState<FileList | null>()
    //const [clientData, setCLientData] = useState<FileList | null>()

    // const borrowerChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setBorrower(e.target.value)
    // }
    //
    // const passportChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setPassport(e.target.files)
    // }
    //
    // const bankProductChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setBankProduct(e.target.value)
    // }
    //
    // const maxSumChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setMaxSum(e.target.value)
    // }
    //
    // const monthPayChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setMonthPay(e.target.value)
    // }
    //
    // const productOfferChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setProductOffer(e.target.value)
    // }
    //
    // const timeChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setTime(e.target.value)
    // }
    //
    // const otherDocChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setOtherDoc(e.target.files)
    // }



    // const moneyChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setMoneyData(e.target.files)
    // }
    //
    // const coborrowerChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setCoBorrower(e.target.value)
    // }
    //
    // const guarantorChangeHandler = (e: React.ChangeEvent<HTMLInputElement>) => {
    //     setGuarantor(e.target.value)
    // }


    return (
        <div>
            {/*<div className={"flex flex-col gap-1 mb-4"}>*/}
            {/*    <label>Укажите участников</label>*/}
            {/*    <div className={'flex flex-col gap-3'}>*/}
            {/*        <Input onChange={borrowerChangeHandler}  placeholder={"Заемщик"}/>*/}
            {/*        <Input onChange={coborrowerChangeHandler} placeholder={"Созаемщик (опционально)"}/>*/}
            {/*        <Input onChange={guarantorChangeHandler} placeholder={"Поручитель (опционально)"}/>*/}
            {/*    </div>*/}
            {/*</div>*/}

            {/*<div className={"flex gap-4 items-end mb-4"}>*/}
            {/*    <div className={'flex flex-col gap-1 w-full'}>*/}
            {/*        <label>Паспорт клиента</label>*/}
            {/*        <DropZone onChange={passportChangeHandler} maxFile={1} ext={'pdf, jpg, png'}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1 w-full'}>*/}
            {/*        <label>Документы, подтверждающие трудовую занятость и доход клиента</label>*/}
            {/*        <DropZone onChange={moneyChangeHandler} maxFile={2} ext={'pdf, jpg, png'}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1 w-full'}>*/}
            {/*        <label>Иные документы, способные повлиять на принятие решения (необязательные)</label>*/}
            {/*        <DropZone onChange={otherDocChangeHandler} maxFile={5} ext={'любые файлы'}/>*/}
            {/*    </div>*/}
            {/*</div>*/}



            {/*<div className={"flex flex-col gap-2"}>*/}
            {/*    <div className={'flex flex-col gap-1'}>*/}
            {/*        <label>Банковский продукт</label>*/}
            {/*        <Input onChange={bankProductChangeHandler} placeholder={"потребительский кредит"}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1'}>*/}
            {/*        <label>Сумма максимальная/запрашиваемая</label>*/}
            {/*        <Input onChange={maxSumChangeHandler} placeholder={"Сумма максимальная"}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1'}>*/}
            {/*        <label>Срок максимальный/запрашиваемый</label>*/}
            {/*        <Input onChange={timeChangeHandler} placeholder={"Срок максимальный"}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1'}>*/}
            {/*        <label>Ставка по продукту/запрашиваемая</label>*/}
            {/*        <Input onChange={productOfferChangeHandler} placeholder={"Ставка по продукту"}/>*/}
            {/*    </div>*/}

            {/*    <div className={'flex flex-col gap-1'}>*/}
            {/*        <label>Ежемесячный платеж</label>*/}
            {/*        <Input onChange={monthPayChangeHandler} placeholder={"Ежемесячный платеж"}/>*/}
            {/*    </div>*/}
            {/*</div>*/}


        </div>
    );
};

export default Form;