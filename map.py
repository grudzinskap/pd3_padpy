import pandas as pd
import plotly
import plotly.graph_objs as go
plotly.tools.set_credentials_file(username='grudzinskap', api_key='DATp56wVmFml5xEGhLej')



def create_map(stacki, g, s, b, date_od, date_do):
    country_codes = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
    country_codes = country_codes.loc[:, ['COUNTRY', 'CODE']]
    country_codes.columns = ['country', 'code']

    users_countries_paths = [r'users_data\e_users_data.csv',
                             r'users_data\m_users_data.csv',
                             r'users_data\p_users_data.csv']


    df = pd.DataFrame(columns=['Id', 'Reputation', 'CreationDate', 'LastAccessDate', 'Views', 'UpVotes',
                               'DownVotes', 'gold', 'silver', 'bronze', 'code', 'stack'])
    for path in users_countries_paths:
        tmp_df = pd.read_csv(path)
        tmp = path.replace('users_data', '').split('_')[0]
        tmp_df['stack'] = tmp[-1]
        df = df.append(tmp_df)

    df = df.query(
        'stack in @stacki and gold >= @g and silver >= @s and bronze >= @b and CreationDate >= @date_od and CreationDate <= @date_do')

    df = pd.DataFrame(df.groupby(['code']).size()).reset_index()
    df.columns = ['code', 'n']

    all_users = df['n'].sum()
    df['proc'] = df['n'].apply(lambda x: str(round(100 * x / all_users, 3)) + '%')

    missing_countries = list(set(country_codes.code) - set(df.code))
    tmp = pd.DataFrame(missing_countries, columns=['code'])
    tmp['n'] = 0
    tmp['proc'] = '0%'
    df = df.append(tmp, sort=False)
    df = pd.merge(df, country_codes, left_on='code', right_on='code')
    df['text'] = df['proc'] + '<br>' + df['country']

    data = [dict(
        type='choropleth',
        locations=df['code'],
        z=df['n'],
        text=df['text'],
        colorscale=[[0, "rgb(5, 10, 172)"], [0.25, "rgb(40, 60, 190)"], [0.5, "rgb(70, 100, 245)"], \
                    [0.7, "rgb(90, 120, 245)"], [0.95, "rgb(106, 137, 247)"], [1, "rgb(220, 220, 220)"]],
        autocolorscale=False,
        reversescale=True,
        marker=dict(
            line=dict(
                color='rgb(180,180,180)',
                width=0.5
            )),
        colorbar=dict(
            autotick=False,
            title='Liczba użytkowników', len=0.5))]

    layout = dict(
        title='Lokalizacja użytkowników',
        width=1200,
        height=650,
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection=dict(type='Mercator'),
        ))

    fig = dict(data=data, layout=layout)
    return fig