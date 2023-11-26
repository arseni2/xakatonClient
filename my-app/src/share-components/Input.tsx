const Input = (props: any) => {
    const {className, ...otherProps} = props
    const classInput = 'p-2 font-medium rounded-[4px] border-[1px] border-borderGray outline-none ' + className
    return <input className={classInput} {...otherProps}/>
};

export default Input;