'''
update_ratestat_tags_from_vote_playlists.py

Created: ?
Modified: 01/22/20


'''

# Do setup processing so that this script can import all the needed modules from the "mlu" package.
# This is necessary because these scripts are not located in the root directory of the project, but
# instead in the 'scripts' folder.
import envsetup
envsetup.PreparePythonProjectEnvironment()

# import external Python modules
import argparse
from prettytable import PrettyTable

# setup logging for this script using MLU preconfigured logger
import mlu.common.logger
mlu.common.logger.initMLULogger()
logger = mlu.common.logger.getMLULogger()

# import project-related modules
import mlu.tags.ratestats

parser = argparse.ArgumentParser()

parser.add_argument("playlistRootDir", 
                    help="absolute filepath of the folder containing the vote playlist files (1.m3u, 2.m3u, ..., 10.m3u) to use as the data source",
                    type=str)

parser.add_argument("playlistArchiveDir", 
                    help="absolute filepath of the folder where the archive of the vote playlist files should be saved for backup after the music rating tags are updated",
                    type=str)

args = parser.parse_args()

# Start the main ratestat tag-writing process
logger.info("Loading audio file votes data from all vote playlists")
audioFileVoteDataList = mlu.tags.ratestats.getAudioFileVoteDataFromRatePlaylists(args.playlistRootDir)

logger.info("New votes data structure filled from vote playlists data successfully")
logger.info("Writing tag data from data structure to audio files")

for audioFileVoteData in audioFileVoteDataList:
    logger.debug("Processing new votes for audio file '{}'".format(songFilepath))
    mlu.tags.ratestats.updateRatestatTags(audioFileVoteData)

logger.info('Music ratestats tag data update completed successfully: {} songs were updated'.format(len(audioFileVoteDataList)))

# Print the results of all updated songs in table form and what changes occurred
tagUpdatesTable = PrettyTable()
tagUpdatesTable.field_names = ["Title", "Artist", "Votes Added", "New Rating", "New Votes List"]

for audioFileVotesData in audioFileVoteDataList:

    tagHandler = mlu.tags.io.AudioFileTagIOHandler(audioFileVotesData.filepath)
    currentTags = tagHandler.getTags()

    votesAdded = mlu.tags.common.formatValuesListToAudioTag(audioFileVotesData.votes)

    tagUpdatesTable.add_row([
        currentTags.title, 
        currentTags.artist, 
        votesAdded,
        currentTags.rating,
        currentTags.votes
    ])

logger.info("\nThe following changes were made to music library:\n{}".format(tagUpdatesTable))

logger.info('Archiving vote playlists...')
mlu.tags.ratestats.archiveRatePlaylists(playlistsDir=args.playlistRootDir, archiveDir=args.playlistArchiveDir)

logger.info('Emptying already counted votes from vote playlists...')
mlu.tags.ratestats.resetRatePlaylists(playlistsDir=args.playlistRootDir)

logger.info('Script complete')