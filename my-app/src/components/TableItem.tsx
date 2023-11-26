import {Link} from "react-router-dom";
type propsType = {
    data: any
}
const TableItem = (props: propsType) => {
    console.log(props.data)
    return (
        <Link className={"contents"} to={"/121212"}>
            <tr className="bg-white hover:bg-gray cursor-pointer">
                <td className="w-4 p-4">
                    <div className="flex items-center">
                        <input id="checkbox-table-3" type="checkbox"
                               className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"/>
                        <label htmlFor="checkbox-table-3" className="sr-only">checkbox</label>
                    </div>
                </td>
                <td scope="row" className="px-6 py-4 whitespace-nowrap">
                    <div className={"flex justify-center"}>{props.data && props.data["ФИО"]}</div>
                </td>
                <td className="px-6 py-4">
                    <div className={"flex justify-center"}>{props.data && props.data["Адрес регистрации"]}</div>
                </td>
                <td className="px-6 py-4">
                    <div className={"flex justify-center"}>{props.data && props.data["Должность"]}</div>
                </td>
                <td className="px-6 py-4">
                    <div className={"flex justify-center"}> {props.data && props.data["Ежемесячный подтвержденный доход по месту работы"]}</div>
                </td>
                <td className="px-6 py-4 ">
                    <div className={"flex justify-center"}>
                        {props.data && props.data["Наличие детей"]}
                    </div>
                </td>
            </tr>
        </Link>
    );
};

export default TableItem;