import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd

# optional: for ggplot-like style
# noinspection PyUnresolvedReferences
mpl.style.use( ['ggplot'] )

df = pd.read_excel( 'Presidential-Runoff-2000-DETAILS.xlsx', sheet_name='Regional' )
pd.set_option( 'display.max_columns', None )
pd.set_option( 'display.max_rows', None )

# copy dataframe to new object
new_df = df.copy()

# change column names
new_df.columns = ['Region', 'Mills', 'Mills%', 'Kuffour', 'Kuffour%', 'Valid', 'Rejects', 'Total Cast', 'Reg. Voters',
                  'Turnout%']

new_df = new_df[['Region', 'Mills', 'Mills%', 'Kuffour', 'Kuffour%']]

# convert percentage data
perc = ['Mills%', 'Kuffour%']

for col in perc:
    new_df[col] = new_df[col]*100

# create row for totals
totals = ['Total']
for col in new_df.columns:
    if col != 'Region':
        totals.append( new_df[col].sum() )

new_df.loc[10] = totals


# change index to regions
new_df.set_index( 'Region', inplace=True )

# convert total percentage
new_df.loc['Total', ['Mills%', 'Kuffour%']] = (new_df.loc['Total', ['Mills%', 'Kuffour%']] / 10)

print( new_df)

# dataframe without Total
no_tot_df = new_df.drop( new_df.index[10] )


# bar chart for number of votes received by each

def bar_chart(dataset):
    ax = dataset.plot.bar( figsize=(10, 5), width=0.5, color=['red','blue'])

    #ax.set_title( input( 'Enter a title for your graph: ' ) )
    #ax.set_xlabel( input( 'Enter a label for the x-axis' ) )
    #ax.set_ylabel( input( 'Enter a label for the y-axis' ) )
    ax.ticklabel_format( style='plain', axis='y' )
    for bar in ax.patches:
        ax.annotate( "{}".format( bar.get_height() ), xy=(bar.get_x() + 0.02, bar.get_height() + 0.01) )
    plt.show()


bar_chart( new_df.loc['Total', ['Mills', 'Kuffour']] )
bar_chart( new_df.loc['Total', ['Mills%', 'Kuffour%']] )
bar_chart( no_tot_df.loc[no_tot_df.index.values.tolist(), ['Mills%', 'Kuffour%']] )
