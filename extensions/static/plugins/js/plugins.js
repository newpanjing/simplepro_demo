new Vue({
    el: "#app",
    data: {
        searchInput: '',
        local: false,
        loading: true,
        tableData: [],
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
    created() {

        var self = this;
        //加载数据
        this.getData('proxy', {
            'method': 'category'
        }).then(res => {
            self.category = res.data;
        }).finally(__ => {
            self.loading = false;
            if(self.category.length!=0){
                self.selectCategory(self.category[0]);
            }
            self.category.unshift({
                id: '-1',
                name: '已安装的'
            });
            // self.$forceUpdate();
        });


    },
    methods: {
        getData(url, data) {
            var self = this;
            return new Promise((resolve, reject) => {
                axios.post(_config.baseUrl + url, data).then(res => {
                    if (res.data.state) {
                        resolve(res.data);
                    } else {
                        reject(res.data);
                        self.$message.error('server error.');
                    }
                }).catch(err => {
                    reject(err);
                    self.$message.error('server error.');
                });
            });
        },
        selectCategory: function (item) {
            this.category.forEach(n => n.active = false);
            item.active = true;
            this.$forceUpdate();
            this.local = item.id == '-1'

            if (item.id == '-1') {
                return;
            }

            var self = this;
            self.getData('proxy', {
                method: 'apps',
                cid: item.id
            }).then(res => {
                self.tableData = res.data;
                console.log(self.tableData)
            });

        }
    }
})