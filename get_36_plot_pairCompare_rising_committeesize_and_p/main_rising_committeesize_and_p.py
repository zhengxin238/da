
from get_36_plot_pairCompare_rising_committeesize_and_p.aggregate_collecttion_pairCompare import final_plot_rising_committee_size_36pics, \
    final_plot_rising_p_1pic



"""

!!!!!!!Before running this func,  we need to run dfs_36_intoDB  and get the data ready for this func!!!!!

Aggregate DataFrames from multiple collections in MongoDB. """

database_name = "DataSet_36pairs"

# final_plot_rising_committee_size_36pics(database_name)
file_name = "pairCompare_rising_p"
final_plot_rising_p_1pic(database_name,file_name)