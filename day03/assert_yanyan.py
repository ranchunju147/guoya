def assert_int():
    try:
        assert 3>2
        assert 3==3
        assert 2<3
    except:
        print('断言失败')
def assert_str():
    try:
        assert '厉害了' in '厉害了中国'
        # assert '厉害了'=='厉害了'
        # assert '厉害了' not in '厉害了中国'
    except:
        print('断言失败')
if __name__ == '__main__':
    assert_str()


