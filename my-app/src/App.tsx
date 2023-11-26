import React, { useState } from 'react';
import * as XLSX from 'xlsx';
import Table from './components/Table';
import DropZone from './components/DropZone';

function App() {
    const [data, setData] = useState<any[]>([]);

    const handleFileUpload = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();

        reader.onload = (event) => {
            const data = new Uint8Array(event.target.result);
            const workbook = XLSX.read(data, { type: 'array' });

            const sheetName = workbook.SheetNames[0];
            const sheet = workbook.Sheets[sheetName];

            const jsonData = XLSX.utils.sheet_to_json(sheet);

            if (jsonData.length > 0) {
                setData(jsonData);
            } else {
                console.log('Empty file or unable to parse.');
            }
        };

        reader.readAsArrayBuffer(file);
    };

    return (
        <div className={'flex justify-center w-full'}>
            <div className={'max-w-[1100px] p-4'}>
                <div className={'flex flex-col gap-1'}>
                    <label>Загрузите данные клиента</label>
                    <DropZone onChange={handleFileUpload} maxFile={1} ext={'xls'} />
                </div>

                <Table data={data} />
            </div>
        </div>
    );
}

export default App;
