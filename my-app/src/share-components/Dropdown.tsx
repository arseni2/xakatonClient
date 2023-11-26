import {useState} from 'react';
import DropdownItem from "./DropdownItem";

type propsType = {
    title: string
}
const Dropdown = (props: propsType) => {
    const [isOpen, setOpen] = useState(false)
    let onClickHandler = () => {
        setOpen(!isOpen)
    };
    return (
        <>
            <div onClick={onClickHandler} className={"cursor-pointer border-[1px] border-borderGray hover:bg-gray-900 focus:outline-none font-medium rounded-[4px] text-sm px-4 py-2.5 me-2 mb-2"}>
                <div className={"flex justify-between"}>
                    <div className={"flex gap-3"}>
                        <svg className="w-5 h-5 text-primary" aria-hidden="true"
                             xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 20 18">
                            <path
                                d="M18.85 1.1A1.99 1.99 0 0 0 17.063 0H2.937a2 2 0 0 0-1.566 3.242L6.99 9.868 7 14a1 1 0 0 0 .4.8l4 3A1 1 0 0 0 13 17l.01-7.134 5.66-6.676a1.99 1.99 0 0 0 .18-2.09Z"/>
                        </svg>
                        {props.title}
                    </div>

                    <div>
                        {isOpen
                            ? <svg className="w-4 h-5 text-primary" aria-hidden="true"
                                   xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                      d="M13 7 7.674 1.3a.91.91 0 0 0-1.348 0L1 7"/>
                            </svg>
                            : <svg className="w-4 h-5 text-primary" aria-hidden="true"
                                   xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 8">
                                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                      d="m1 1 5.326 5.7a.909.909 0 0 0 1.348 0L13 1"/>
                            </svg>
                        }

                    </div>
                </div>
            </div>

            {isOpen
                &&  <div className={"absolute bg-white divide-y divide-gray-100 rounded-lg shadow w-[522px]"}>
                    <DropdownItem title={"Риску"} />
                </div>
            }
        </>
    );
};

export default Dropdown;