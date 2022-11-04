
interface IList{
item: []
}


class list {
    item: IList
    constructor(items:IList){
        this.item =items
    }

    print = () => {
    this.item.item.map(x => console.log(x)
    )
    }
}