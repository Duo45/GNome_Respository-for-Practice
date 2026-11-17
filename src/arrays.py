import numpy as np
ELEMENTS=np.array(["Li","Fe","P","O"])
ELEMENT_NUMBERS = np.array([3, 26, 15, 8], dtype=np.int64)#元素周期表上原子序数
COMPOSITIONS = np.array(
    [
        [1, 1, 1, 4],   # LiFePO4
        [0, 2, 0, 3],   # Fe2O3
        [2, 0, 0, 1],   # Li2O
    ],
    dtype=np.float64,
)

LATTICES = np.array(
    [
        [
            [4.0, 0.0, 0.0],
            [0.0, 4.0, 0.0],
            [0.0, 0.0, 8.0],
        ],
        [
            [3.5, 0.0, 0.0],
            [0.0, 3.5, 0.0],
            [0.0, 0.0, 5.0],
        ],
    ],
    dtype=np.float64,
)


def show_array_info(name, array):
    """打印数组的名称、形状、类型、最小值和最大值。"""
    array = np.asarray(array)

    print(f"\n{name}")
    print("shape:", array.shape)
    print("dtype:", array.dtype)

    if array.size == 0:
        print("数组为空")
        return

    print("最小值:", array.min())
    print("最大值:", array.max())


def scaled_one_hot(element_ids, ratios, num_elements):
    """把元素编号转为独热编码，并乘上对应的化学计量比。"""
    ids = np.asarray(element_ids)
    ratio_values = np.asarray(ratios)

    # 按照要求，首先打印输入形状。
    print("元素编号形状:", ids.shape)
    print("化学比例形状:", ratio_values.shape)

    # 元素编号和比例都必须是一维。
    if ids.ndim != 1 or ratio_values.ndim != 1:
        raise ValueError("输入必须是一维数组")

    # 每一条元素编号都必须有对应的比例。
    if ids.shape != ratio_values.shape:
        raise ValueError("元素编号和比例数量必须相同")

    # 不能把 True 当成元素种类数。
    if isinstance(num_elements, bool):
        raise TypeError("元素种类数必须是正整数")

    if not isinstance(num_elements, (int, np.integer)):
        raise TypeError("元素种类数必须是正整数")

    num_elements = int(num_elements)

    if num_elements <= 0:
        raise ValueError("元素种类数必须大于 0")

    # 非空编号必须是整数类型。
    if ids.size > 0 and not np.issubdtype(ids.dtype, np.integer):
        raise TypeError("元素编号必须是整数")

    # 元素编号必须位于 0 到 num_elements - 1 之间。
    if ids.size > 0:
        has_negative = np.any(ids < 0)
        has_too_large = np.any(ids >= num_elements)

        if has_negative or has_too_large:
            raise ValueError(
                f"元素编号必须位于 0 到 {num_elements - 1} 之间"
            )

    # 把比例转换为小数；转换失败时给出明确错误。
    try:
        ratio_values = ratio_values.astype(np.float64)
    except (TypeError, ValueError) as error:
        raise TypeError("化学比例必须是数字") from error

    # 比例不能是 NaN、无穷大、0 或负数。
    if not np.all(np.isfinite(ratio_values)):
        raise ValueError("化学比例必须是有限数字")

    if np.any(ratio_values <= 0):
        raise ValueError("化学比例必须大于 0")

    # 每条记录占一行，每个元素占一列。
    result = np.zeros(
        (len(ids), num_elements),
        dtype=np.float64,
    )

    for i in range(len(ids)):
        row = i
        column = ids[i]
        ratio = ratio_values[i]
        result[row, column] = ratio

    return result


def main():
    print("元素顺序:", ELEMENTS)

    show_array_info("元素编号数组", ELEMENT_NUMBERS)
    show_array_info("成分矩阵", COMPOSITIONS)
    show_array_info("晶格张量", LATTICES)

    print("\n每行求和 sum(axis=1):")
    print(COMPOSITIONS.sum(axis=1))

    print("\n每列求和 sum(axis=0):")
    print(COMPOSITIONS.sum(axis=0))

    print("\n每个晶格向量三个分量的和 sum(axis=2):")
    print(LATTICES.sum(axis=2))

    result = scaled_one_hot(
        element_ids=[0, 3],
        ratios=[2.0, 1.0],
        num_elements=4,
    )

    print("\nLi2O 的两条缩放独热记录:")
    print(result)

    print("\nLi2O 整体成分向量 sum(axis=0):")
    print(result.sum(axis=0))


if __name__ == "__main__":
    main()
