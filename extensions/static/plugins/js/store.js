Vue.component('store', {
    props: ['tableData'],
    data() {
        return {
            headers: [{
                label: '插件名',
                field: 'name'
            }, {
                label: '介绍',
                field: 'short_description'
            }, {
                label: '作者',
                field: 'user'
            },
                // {
                // label: '价格',
                // field: 'amount'
            // },
                {
                label: '下载量',
                field: 'downloads'
            }, {
                label: '版本',
                field: 'version'
            }]
        }
    },
    template: `
         <el-table :data="tableData" style="width: 100%">
                <el-table-column v-for="item in headers"
                                 :prop="item.field"
                                 :label="item.label"
                                 :key="item.field">
                </el-table-column>

                <el-table-column
                        prop="options"
                        label="操作">
                    <el-button size="small" type="success">安装</el-button>
                    <el-button size="small" type="danger">卸载</el-button>
                </el-table-column>
            </el-table>
    `
});