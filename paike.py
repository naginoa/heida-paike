def get_Dict(filename, key):
    with open(filename, encoding='utf-8') as f:
        _dict = {}
        i = 1
        key.append('id')
        key.append('flag')
        for line in f.readlines():
            _list = []
            _list = line.strip('\n').strip('\ufeff').split('，')
            _list.append(0)
            _list.append(0)
            sub_dict = dict(zip(key, _list))
            _dict.update({i:sub_dict})
            i = i + 1
    return _dict	

	
def show_dictprettify(filenames, keys):
    for filename, key in zip(filenames, keys):
        for i in get_Dict(filename, key).items():
           print(i)


def paike_result(Id):
    Sum = 0
    for s in coursedict:
        if coursedict.get(s)['周一'] != '00000000':
            Sum += 1
    shengyu = Sum
    #while shengyu <= Sum:
    for s in coursedict:
        if coursedict.get(s)['周一'] != '00000000':
            coursedict.get(s)['id'] = Id
            Id += 1
            print(coursedict.get(s)['周一'])
            clac = len(roomdict)
            a = 1
            p = int(roomdict.get(a)['人数'])
            Max = p
            while (a <= 17):
                q = int(roomdict.get(int(a)+1)['人数'])
                if Max <= q:
                    Max = q
                a = a + 1
            print(Max)





if __name__ == '__main__':
    keys = [['学院','专业','班级','周一','周二','周三','周四','周五'],['老师','文理'],['机房','人数','周一','周二','周三','周四','周五']]
    filenames = ['课程表.txt','教师.txt','机房.txt']
    Id = 1
    coursedict = get_Dict(filenames[0], keys[0])
    teacherdict = get_Dict(filenames[1], keys[1])
    roomdict = get_Dict(filenames[2], keys[2])
    show_dictprettify(filenames, keys)
    paike_result(Id)
