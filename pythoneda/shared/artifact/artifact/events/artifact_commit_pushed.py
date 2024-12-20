# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/artifact/artifact_commit_pushed.py

This file declares the ArtifactCommitPushed event.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/artifact-events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.artifact.events import AbstractCommitPushed, Change
from typing import List


class ArtifactCommitPushed(AbstractCommitPushed):
    """
    Represents the moment a commit has been pushed.

    Class name: ArtifactCommitPushed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact.events.artifact.ArtifactChangesCommitted: A previous event that wraps the commit.
    """

    def __init__(
        self,
        change: Change,
        commit: str,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new ArtifactCommitPushed instance.
        :param change: The change.
        :type change: pythoneda.shared.artifact.Change
        :param commit: The hash of the commit.
        :type commit: str
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            change,
            commit,
            previousEventIds,
            reconstructedId,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
