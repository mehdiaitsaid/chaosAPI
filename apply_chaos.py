def apply_chaos(testcase):
    import random
    chaotic_testcase = testcase.copy()
    if random.choice([True, False]):
        chaotic_testcase['parameters'] = {key: "CHAOS" for key in testcase['parameters']}
    return chaotic_testcase