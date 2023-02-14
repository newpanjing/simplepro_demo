let data = [{
    "value": 15,
    "label": "广东",
    "children": [{"value": 16, "label": "东莞"}, {
        "value": 17,
        "label": "深圳",
        "children": [{
            "value": 20,
            "label": "龙华区",
            "children": [{"value": 27, "label": "龙华街道"}, {"value": 28, "label": "清湖街道"}]
        }, {
            "value": 29,
            "label": "龙岗区",
            "children": [{"value": 30, "label": "象角塘社区", "children": [{"value": 31, "label": "佳兆业广场"}]}]
        }]
    }]
}, {
    "value": 18,
    "label": "北京",
    "children": [{"value": 19, "label": "朝阳区", "children": [{"value": 33, "label": "213"}]}]
}, {"value": 21, "label": "山东", "children": [{"value": 22, "label": "青岛"}]}, {
    "value": 23,
    "label": "福建",
    "children": [{
        "value": 24,
        "label": "厦门",
        "children": [{"value": 25, "label": "思明区"}, {"value": 26, "label": "湖里区"}]
    }]
}]

function deepFind(data, value) {
   // 递归查找，获取value的所有父级id
    let result = []
    for (let i = 0; i < data.length; i++) {
        if (data[i].value === value) {
            result.push(data[i].value)
            return result
        } else if (data[i].children) {
            let temp = deepFind(data[i].children, value)
            if (temp.length > 0) {
                result.push(data[i].value)
                return result.concat(temp)
            }
        }
    }
    return result
}

console.log(deepFind(data, 31))
