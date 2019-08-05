import csvmatch
import pandas as pd


def fuzzy_merge(df1,
          df2,
          on=None,
          left_on=None,
          right_on=None,
          keep=None,
          keep_left='all',
          keep_right='all',
          method='exact',
          threshold=0.6,
          **kwargs):
    """Fuzzy matching between two dataframes

    Parameters
    ----------
    left : DataFrame
    right : DataFrame
        Object to merge left with
    on : str or list
        Column names to compare. These must be found in both DataFrames.
    left_on : str or list
        Column names to compare in the left DataFrame.
    right_on : str or list
        Column names to compare in the right DataFrame.
    keep : str { 'all', 'match' }
        Overrides keep_left and keep_right
    keep_left : str or list, default 'all'
        List of columns to preserve from the left DataFrame.
        If 'all', preserve all columns.
        If 'match', preserve left_on matching) column.
        If any other string, just keeps that one column.
    keep_right : str or list, default 'all'
        List of columns to preserve from the right DataFrame.
        If 'all', preserve all columns. Defaults to right_on.
        If 'match', preserve right_on (matching) column.
        If any other string, just keeps that one column.
    method : str or list, default 'exact'
        Perform a fuzzy match, and an optional specified algorithm.
        Multiple algorithms can be specified which will apply to each field
        respectively.

        * exact: exact matches
        * levenshtein: string distance metric
        * jaro: string distance metric
        * metaphone: phoenetic matching algorithm
        * bilenko: prompts for matches

    threshold : float or list, default 0.6
        The threshold for a fuzzy match as a number between 0 and 1
        Multiple numbers will be applied to each field respectively
    ignore_case : bool, default False
        Ignore case (default is case-sensitive)
    ignore_nonalpha : bool, default False
        Ignore non-alphanumeric characters
    ignore_nonlatin : bool, default False
        Ignore characters from non-latin alphabets
        Accented characters are compared to their unaccented equivalent
    ignore_order_words : bool, default False
        Ignore the order words are given in
    ignore_order_letters : bool, default False
        Ignore the order the letters are given in, regardless of word order
    ignore_titles : bool, default False
        Ignore a predefined list of name titles (such as Mr, Ms, etc)
    join : { 'inner', 'left-outer', 'right-outer', 'full-outer' }

    Returns
    -------
    pd.DataFrame
        a DataFrame of matchine rows
    """
    data1 = df1.values.tolist()
    headers1 = list(df1.columns)

    data2 = df2.values.tolist()
    headers2 = list(df2.columns)

    if not isinstance(threshold, list):
        threshold = [threshold]

    if on:
        left_on = on
        right_on = on

    if not isinstance(left_on, list):
        left_on = [left_on]

    if not isinstance(right_on, list):
        right_on = [right_on]

    if keep:
        keep_left = keep
        keep_right = keep

    if keep_left == 'all':
        keep_left = headers1
    if keep_right == 'all':
        keep_right = headers2

    if keep_left == 'match':
        keep_left = left_on
    if keep_right == 'match':
        keep_right = right_on

    if isinstance(keep_left, str):
        keep_left = [keep_left]

    if isinstance(keep_right, str):
        keep_right = [keep_right]

    output = []
    output.extend(['1.' + col for col in (keep_left or left_on)])
    output.extend(['2.' + col for col in (keep_right or right_on)])

    if not isinstance(method, list):
        method = [method]

    output = kwargs.pop('output', output)

    results, keys = csvmatch.run(
        data1,
        headers1,
        data2,
        headers2,
        fields1=left_on,
        fields2=right_on,
        thresholds=threshold,
        output=output,
        methods=method,
        **kwargs)

    return pd.DataFrame(results, columns=keys)
