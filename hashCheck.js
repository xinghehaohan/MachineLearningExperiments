function _0x3eb1b2(code) {
    const lookup = {
        0x3f13: 'length',
        0x10ee: 'type',
        0x23f5: 'value',
        0x2b63: 'key',
        0x44eb: 'handlers',
        0x228a: 'next',
        0x3df9: 'func'
    };
    return lookup[code] || '';
}

function _0x376a7f(code) {
    const lookup = {
        0x22d7: 'specific_type',
        0x3cdf: 'error',
        0x377d: 'Error: '
    };
    return lookup[code] || '';
}

function _0x55f3dd(code) {
    const lookup = {
        0x1718: 'get',
        0x112d: 'some_key',
        0x949: 'some_default',
        0x1942: 'forEach'
    };
    return lookup[code] || '';
}

function _0x3c7960(code) {
    const lookup = {
        0x10ee: 'type',
        0x23f5: 'value',
        0x1942: 'forEach'
    };
    return lookup[code] || '';
}

function _0x3a33c5(code) {
    const lookup = {};
    return lookup[code] || '';
}

// 假设 _0x311576 是一个处理函数
function _0x311576(value) {
    console.log('Processing:', value);
}

function _0x5bb72a(_0x1820e3) {
    var _0xe0c865 = _0x3eb1b2,
        _0x46f34e = _0x376a7f,
        _0x4287e7 = _0x3c7960,
        _0x6b4936 = _0x55f3dd,
        _0x2f1a64 = _0x3a33c5;

    let _0x240f7d = arguments[_0xe0c865(0x3f13)] > 1 && void 0 !== arguments[1] ? arguments[1] : [];
    try {
        let _0x45bbb3;
        if (_0x46f34e(0x22d7) === _0x1820e3[_0x4287e7(0x10ee)]) {
            _0x45bbb3 = _0x1820e3[_0x4287e7(0x23f5)];
            _0x311576(_0x1820e3[_0xe0c865(0x2b63)]);
        } else {
            _0x45bbb3 = _0x1820e3[_0x1820e3[_0x6b4936(0x10ee)]];
        }
        _0x311576(_0x45bbb3);
        _0x240f7d[_0x6b4936(0x1942)](_0x524bce => {
            _0x311576(_0x524bce);
        });
        (_0x1820e3[_0x6b4936(0x44eb)] || []).forEach(_0x426fea => {
            _0x311576(_0x426fea);
        });
        if (_0x1820e3[_0x46f34e(0x228a)]) {
            _0x5bb72a(_0x1820e3[_0x46f34e(0x228a)][_0xe0c865(0x3df9)]);
        }
    } catch (_0x3c4f9f) {
        console[_0x46f34e(0x3cdf)](_0x46f34e(0x377d), _0x3c4f9f);
    }
}

function _0x5c51c8(_0x4d7e18) {
    var _0x4c1270 = _0x55f3dd,
        _0x154c4c = _0x55f3dd,
        _0x53c773 = _0x3eb1b2,
        _0x5ee2ed = _0x376a7f;

    _0x5bb72a(_0x4d7e18[_0x4c1270(0x1718)](_0x154c4c(0x112d)), _0x4d7e18[_0x154c4c(0x1718)](_0x154c4c(0x949)) || []);
}

// 测试解混淆后的函数
function test() {
    const testData = {
        get: (key) => {
            if (key === 'some_key') return 'value_for_some_key';
            if (key === 'some_default') return 'default_value';
            return null;
        }
    };

    console.log('Test Case 1:');
    _0x5c51c8(testData);

    console.log('Test Case 2:');
    _0x5bb72a({
        type: 'specific_type',
        value: 'some_value',
        key: 'some_key',
        handlers: ['handler1', 'handler2'],
        next: {
            func: 'next_func'
        }
    });

    console.log('Test Case 3:');
    _0x5bb72a({
        type: 'other_type',
        some_other_key: 'some_value',
        handlers: ['handler3', 'handler4']
    });
}

test();
