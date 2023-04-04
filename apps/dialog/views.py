from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from dialog.models import Dialog


def test1(request):
    return render(request, 'dialog/test1.html')


def test2(request):
    # 这里通过request.GET可以拿到id
    pk = request.GET.get('id')
    # 然后通过id 拿到model
    dialog = Dialog.objects.get(pk=pk)
    return render(request, 'dialog/test2.html', {
        'dialog': dialog
    })


def ajax(request):
    """
    返回ajax数据
    """

    ds = []
    for i in range(30):
        name = '小红'
        if i % 2 == 0:
            name = '小明'
        ds.append({
            'value': i,
            'label': name
        })
    return JsonResponse({'ds': ds})
