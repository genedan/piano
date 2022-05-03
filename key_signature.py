def generate_key_signature(key, clef, scale_type):
    """
    Function that generates the front of Anki cards for drilling key signatures. For example, the card for D major
    should look like:

    {
        \clef treble
        \key d \major
        \override Staff.TimeSignature.transparent = ##t
        s2 s2
    }

    :param key:
    :param clef:
    :param scale_type:
    :return:
    """
    res = "{\n"
    res += "    \clef " + clef + "\n"
    res += "    \key " + key + " \\" + scale_type + "\n"
    res += "    \override Staff.TimeSignature.transparent = ##t\n"
    res += "    s2 s2\n"
    res += "}"

    return res
