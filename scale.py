import random

minor_scales = [
    'A Minor',
    'E Minor',
    'B Minor',
    'F# Minor',
    'C# Minor',
    'G# Minor',
    'D# Minor',
    'A# Minor',
    'D Minor',
    'G Minor',
    'C Minor',
    'F Minor',
    'Bb Minor',
    'Eb Minor',
    'Ab Minor'
]

major_scales = [
    'C Major',
    'G Major',
    'D Major',
    'A Major',
    'E Major',
    'B Major',
    'F# Major',
    'C# Major',
    'F Major',
    'Bb Major',
    'Eb Major',
    'Ab Major',
    'Db Major',
    'Gb Major',
    'Cb Major',
]


def scale_picker(scale_type):
    if scale_type in ['major', 'dur']:
        return random.choice(major_scales)
    elif scale_type == ['minor', 'moll']:
        return random.choice(major_scales)
    else:
        raise ValueError("Invalid scale type specified.")