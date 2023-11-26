import DetailPagesItem from "../components/DetailPagesItem";

const DetailPages = () => {
    return (
        <div className={"flex justify-center mt-2"}>
            <div className={"flex flex-col w-full max-w-[750px] divide-y divide-borderGray"}>
                <DetailPagesItem />
                <DetailPagesItem isError/>
            </div>
        </div>
    );
};

export default DetailPages;