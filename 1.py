def calculate_water_usage():
    """
    统计水资源消耗量的函数
    """
    # 定义不同活动的水资源消耗标准（单位：升）
    water_usage = {
        '刷牙': 1,
        '洗脸': 6,
        '洗手': 2,
        '淋浴': 15,
        '盆浴': 50,
        '冲厕所': 6,
        '做饭': 8,
        '洗碗': 15,
        '洗衣服': 50,
        '洗车': 200
    }
    
    total_water = 0
    activities = []
    
    print("=== 水资源消耗量统计 ===")
    print("以下是常见活动的水资源消耗标准：")
    for activity, usage in water_usage.items():
        print(f"{activity}: {usage} 升")
    print()
    
    while True:
        activity = input("请输入活动名称（输入'结束'退出）: ")
        if activity == '结束':
            break
        
        if activity not in water_usage:
            print(f"抱歉，'{activity}'不在我们的活动列表中，请输入列表中的活动。")
            continue
        
        try:
            times = int(input(f"请输入{activity}的次数: "))
            if times < 0:
                print("次数不能为负数，请重新输入。")
                continue
        except ValueError:
            print("请输入有效的数字。")
            continue
        
        usage = water_usage[activity] * times
        total_water += usage
        activities.append((activity, times, usage))
        print(f"{activity} {times}次，消耗{usage}升水。")
        print()
    
    print("=== 统计结果 ===")
    if activities:
        print("您的活动记录：")
        for activity, times, usage in activities:
            print(f"{activity}: {times}次，{usage}升")
        print(f"总水资源消耗量：{total_water}升")
        
        # 提供简单的分析和建议
        if total_water < 100:
            print("您的水资源消耗较低，继续保持！")
        elif total_water < 300:
            print("您的水资源消耗适中，可以考虑进一步节约。")
        else:
            print("您的水资源消耗较高，建议采取节水措施。")
        
        print("\n节水建议：")
        print("1. 刷牙时关闭水龙头")
        print("2. 缩短淋浴时间")
        print("3. 收集雨水用于浇花")
        print("4. 修复漏水的水龙头")
    else:
        print("您没有输入任何活动记录。")

if __name__ == "__main__":
    calculate_water_usage()