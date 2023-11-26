import React from 'react';
import TableItem from "./TableItem";
import Input from "../share-components/Input";
import Dropdown from "../share-components/Dropdown";

type propsType = {
    data: any
}
const Table = (props: propsType) => {

    return (
        <div>
            <div className="relative overflow-x-auto shadow-md sm:rounded-lg">
                <div className="flex gap-2 mt-3">
                    <div className="w-full">
                       <Dropdown title={"Сортировать по"} />
                    </div>

                    <div className="w-full flex flex-column sm:flex-row flex-wrap space-y-4 sm:space-y-0 items-center justify-between pb-4">
                        <label htmlFor="table-search" className="sr-only">
                            Search
                        </label>
                        <div className="w-full relative">
                            <div
                                className="absolute inset-y-0 left-0 rtl:inset-r-0 rtl:right-0 flex items-center ps-3 pointer-events-none">
                                <svg className="w-5 h-5 text-primary" aria-hidden="true"
                                     fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                                    <path fill-rule="evenodd"
                                          d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                                          clip-rule="evenodd"></path>
                                </svg>

                            </div>
                            <Input
                                type="text"
                                id="table-search"
                                className="block p-2 ps-10 w-full bg-gray-50"
                                placeholder="Поиск"
                            />
                        </div>
                    </div>
                </div>
                <table className="w-full text-sm text-gray-500">
                    <thead className="text-gray-700 bg-gray">
                    <tr>
                        <th scope="col" className="p-4">
                            <div className="flex items-center">
                                <input id="checkbox-all-search" type="checkbox"
                                       className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"/>
                                <label htmlFor="checkbox-all-search" className="sr-only">checkbox</label>
                            </div>
                        </th>
                        <th scope="col" className="px-6 py-3 font-semibold">
                            ФИО
                        </th>
                        <th scope="col" className="px-6 py-3 font-semibold">
                            Адрес регистрации
                        </th>
                        <th scope="col" className="px-6 py-3 font-semibold">
                            Должность
                        </th>
                        <th scope="col" className="px-6 py-3 font-semibold">
                            Ежемесячный подтвержденный доход
                        </th>
                        <th scope="col" className="px-6 py-3 font-semibold">
                            Наличие детей
                        </th>
                    </tr>
                    </thead>
                    <tbody className={"divide-y divide-gray"}>
                        <TableItem data={props.data[0] && props.data[0]}/>
                    </tbody>
                </table>
            </div>


        </div>
    );
};

export default Table;