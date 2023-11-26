import React from 'react';

type propsType = {
    ext: string
    onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
    maxFile: number
}
const DropZone = (props: propsType) => {
    return (
        <div className={"flex flex-col gap-3"}>
                <label htmlFor="dropzone-file"
                       className="flex flex-col items-center justify-center h-64 border-2 border-primary border-dashed rounded-lg cursor-pointer bg-gray">
                    <div className="flex flex-col items-center justify-center pt-5 pb-6">
                        <svg className="w-8 h-8 mb-4 text-primary" aria-hidden="true"
                             xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 20 16">
                            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2"
                                  d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"/>
                        </svg>
                        <p className="mb-2 text-sm text-gray-500 dark:text-gray-400"><span className="font-semibold">Нажмите для загрузки</span> или
                            перетащите </p>
                        <p className="text-xs text-gray-500 dark:text-gray-400">
                            {props.ext}
                        </p>
                    </div>
                    <input onChange={(e) => props.onChange(e)} accept={props.ext} id="dropzone-file" type="file" multiple={props.maxFile > 1} className="hidden"/>
                </label>
        </div>
    );
};

export default DropZone;