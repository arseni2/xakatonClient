import React from 'react';

const ButtonPrimary = (props: any) => {
    const { children, className} = props
    return (
        <div className={`bg-primary rounded-lg px-[18px] py-[11px] text-white w-fit cursor-pointer font-medium hover:bg-primaryHovered flex justify-center ${className}`}>
            {children}
        </div>
    );
};

export default ButtonPrimary;