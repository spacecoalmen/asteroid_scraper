from numpy.core.umath import radians


def normalize_asteroids(df):
    df.rename(columns={'e': 'ecce',
                       'i': 'incl',
                       'a': 'semiax',
                       'om': 'Omega',
                       'w': 'omegap'}, inplace=True)

    # it's ugly but it seems to work only in this way
    df['incl'] = radians(df['incl'])
    df['Omega'] = radians(df['Omega'])
    df['omegap'] = radians(df['omegap'])
    return df


