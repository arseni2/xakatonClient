import React from 'react';

type propsType = {
    isError?: boolean
}
const DetailPagesItem = (props: propsType) => {
    return (
        <div className={`rounded-md flex justify-between p-3 ${props.isError && "bg-errorBg"} `}>
            <div className={"font-semibold"}>Имя:</div>
            <div>Пупкин Василий Николаевич</div>
        </div>
    );
};

export default DetailPagesItem;