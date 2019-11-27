new Vue({
    el: "#app",
    data: {
        searchInput: '',
        tableData:[],
        tableHeader:[{
            label:'插件名',
            field:'name'
        },{
            label:'介绍',
            field:'short_description'
        },{
            label:'作者',
            field:'author'
        },{
            label:'价格',
            field:'amount'
        },{
            label:'下载量',
            field:'download'
        },{
            label:'版本',
            field:'version'
        }],
        category: [{
            id: '0',
            text: '全部',
            active: true
        }, {
            id: '1',
            text: '应用'
        }, {
            id: '2',
            text: '工具'
        }, {
            id: '3',
            text: '云储存'
        }, {
            id: '5',
            text: '辅助增强'
        }, {
            id: '6',
            text: '未归类'
        }]
    },
    methods: {
        selectCategory: function (item) {
            this.category.forEach(n => n.active = false);
            item.active = true;
            this.$forceUpdate();
        }
    }
})