import pandas as pd
import itertools as it
import numpy as np


def freq_table(x, hue=None, col=None):
    """

    """
    if col is not None and hue is None:
        hue = col.copy()
        col = None

    if hue is None and col is None:
        x_ind = x[x == "?"].index
        x.drop(x_ind, inplace=True)

        tbl = pd.DataFrame(x.value_counts())
        N = x.value_counts().sum()
        tbl["Percentages"] = np.round(100 * tbl[x.name] / N, decimals=2)

        return [(tbl, N)]

    elif hue is not None and col is None:
        drp_indx = x[(x == "?") | (hue == "?")].index
        x.drop(drp_indx, inplace=True)
        hue.drop(drp_indx, inplace=True)

        dumb_df = pd.get_dummies(x)
        dumb_df[hue.name] = hue

        raw = dumb_df.groupby(by=hue.name).sum()

        N = x.value_counts().sort_index().values
        scaled = raw.copy()
        for idx in raw.index:
            scaled.loc[idx] = raw.loc[idx].values / N * 100

        return [(np.round(scaled, decimals=2), N)]

    else:
        tables = []
        drp_indx = x[(x == "?") | (hue == "?") | (col == "?")].index
        x.drop(drp_indx, inplace=True)
        hue.drop(drp_indx, inplace=True)
        col.drop(drp_indx, inplace=True)

        df = pd.get_dummies(x)
        df[hue.name] = hue
        df[col.name] = col

        for column in df[col.name].unique():
            df_col = df[df[col.name] == column]

            grouped = df_col.groupby(by=hue).sum()

            N = x[col == column].value_counts().sort_index().values

            scaled = grouped.copy()
            for idx in grouped.index:
                scaled.loc[idx] = grouped.loc[idx].values / N * 100

            scaled.index.name = f"{column}"
            tables.append((np.round(scaled, decimals=2), len(df_col)))

        return tables


def freq_df(x, hue=None, col=None):
    """
    
    """
    x_name = x.name
    sort_order = x_name
    if hue is not None:
        hue_name = hue.name
        sort_order = hue_name
    if col is not None:
        col_name = col.name

    tbls = freq_table(x, hue=hue, col=col)
    df_list = []
    for dft, N in tbls:
        te = pd.DataFrame(
            [
                (x, hue, vals)
                for (hue, x), vals in zip(
                    it.product(dft.index, dft.columns), dft.values.flatten()
                )
            ]
        )

        if hue is not None:
            te.columns = [x_name, hue_name, "Percentage"]
        else:
            te.columns = [x_name, "Percentage"]
        if col is not None:
            te[col_name] = dft.index.name
        df_list.append(te)

    df = pd.concat(df_list, ignore_index=True)
    df.sort_values(by=sort_order, inplace=True)

    return df, tbls
