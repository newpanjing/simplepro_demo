from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from dialog.models import Dialog
from simplepro.dialog import ModalDialog, MultipleCellDialog


@admin.register(Dialog)
class DialogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'custom_row_btn', 'dialog_url', 'async_load', 'dialog_lists')
    search_fields = ('name',)

    def custom_row_btn(self, *args, **kwargs):
        # 从4.0开始 支持element-ui的组件
        return format_html(
            """
            <a href="javascript:;">查看详情</a>
            <el-button type="success" icon="el-icon-check" circle @click="$message('这是一条消息提示')"></el-button>
            <el-button type="danger" icon="el-icon-refresh" circle @click="app.refreshData()"></el-button>
            """)

    custom_row_btn.short_description = 'elementui的组件'

    def dialog_url(self, model):
        modal = ModalDialog()
        modal.cell = '<el-link type="primary">点击查看</el-link>'
        modal.title = "详情对话框"
        # 这里的url可以写死，也可以用django的方向获取url，可以根据model的数据，传到url中
        modal.url = reverse('dialog:test1') + "?id=%s" % model.id
        modal.show_cancel = True

        return modal

    dialog_url.short_description = '弹出对话框'

    # 这个自定义的对话框，可以在admin也可以在model中声明
    def async_load(self, model):
        modal = ModalDialog()
        modal.height = '500px'
        modal.width = '800px'
        modal.cell = f"{model.id}-异步加载"
        modal.show_cancel = False
        modal.url = reverse('dialog:test2') + "?id=%s" % model.id
        return modal

    async_load.short_description = '异步加载'

    def dialog_lists(self, model):
        return MultipleCellDialog([
            ModalDialog(url='https://simpleui.72wo.com', title='Simple社区'),
            ModalDialog(url='https://simpleui.72wo.com/docs/simplepro', title='SimplePro文档',
                        cell='<el-link type="primary">文档</el-link>'),
        ])

    dialog_lists.short_description = '对话框列表'
