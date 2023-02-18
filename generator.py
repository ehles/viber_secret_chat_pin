
COUNT = 10_000
DELAY = 900

SORT = True

if SORT:
    filename = 'pins_reset_full_sorted.txt'
else:
    filename = 'pins_reset_full.txt'

MAJOR_NUMS = {
    '5': 5,
    '7': 3,
    '3': 1,
}

class Pin:
    def __init__(self, index: int) -> None:
        self.index = index
        self._weight = 0

    def __str__(self):
        return f'{self.index:04}'

    __repr__ = __str__

    @property
    def weight(self):
        if self._weight > 0:
            return self._weight

        weight = 0

        for i, val in enumerate(str(self.index)):
            if val in MAJOR_NUMS:
                weight += MAJOR_NUMS[val] * (4 - int(i))
        self._weight = weight

        return self._weight

    def __lt__(self, other: 'Pin') -> bool:
        return self.weight < other.weight

    def __eq__(self, other: 'Pin') -> bool:
        return self.weight == other.weight


# def generate():
#     rows = []
#     rows.append(f'DEFAULT_DELAY {DELAY}')
#     for mul in range(10):
#         # filename = mul * 1_000
#         for i in range(1_000):
#             index = mul * 1_000 + i
#             rows.append(f'STRING {index:04}')
#             rows.append('CTRL a')
#     with open(f'pins_{filename:04}.txt', 'wt') as fio:
#         fio.write('\n'.join(rows))

def generate() -> list[Pin]:
    pins = []
    for i in range(COUNT):
        pins.append(Pin(i))
    return pins

def sort_pins(pins: list[Pin])-> None:
    pins.sort(reverse=True)

def save(pins: list[Pin]) -> None:
    rows = []
    rows.append(f'DEFAULT_DELAY {DELAY}')
    for p in pins:
        ps = str(p)

        # rows.append(f'STRING {ps:04}-> {p.weight}')
        rows.append(f'STRING {ps}')
        rows.append('CTRL a')
        rows.append(f'STRING 0000')

    with open(filename, 'wt') as fio:
        fio.write('\n'.join(rows))

def save_reset(pins: list[Pin]) -> None:
    rows = []
    rows.append(f'DEFAULT_DELAY {DELAY}')
    for p in pins:
        ps = str(p)

        # rows.append(f'STRING {ps:04}-> {p.weight}')
        rows.append(f'STRING {ps}')
        rows.append(f'STRING 0000')
        rows.append(f'STRING 0000')
        # rows.append(f'DELAY 500')
        rows.append(f'ESC')
        # rows.append(f'DELAY 500')
        rows.append(f'ENTER')
        # rows.append(f'DELAY 500')
        rows.append(f'')

    with open(filename, 'wt') as fio:
        fio.write('\n'.join(rows))


pins = generate()
if SORT:
    sort_pins(pins)
save_reset(pins)