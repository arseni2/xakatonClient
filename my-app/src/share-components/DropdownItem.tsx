import React from 'react';

type propsType = {
    title: string
}
const DropdownItem = (props: propsType) => {
    return (
        <div className={"p-4 cursor-pointer hover:bg-gray"}>
            {props.title}
        </div>
    );
};

export default DropdownItem;