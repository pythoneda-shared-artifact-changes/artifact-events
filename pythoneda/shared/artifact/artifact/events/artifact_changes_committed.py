# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/artifact/artifact_changes_committed.py

This file declares the ArtifactChangesCommitted event.

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
from pythoneda.shared.artifact.events import AbstractChangesCommitted, Change
from typing import List


class ArtifactChangesCommitted(AbstractChangesCommitted):
    """
    Represents the moment artifact changes have been committed.

    Class name: ArtifactChangesCommitted

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - pythoneda.shared.artifact.events.TagPushed: The event this one is response to.
    """

    def __init__(
        self,
        change: Change,
        commit: str,
        tagPushedId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ArtifactChangesCommitted instance.
        :param change: The change information.
        :type change: pythoneda.shared.artifact.Change
        :param commit: The hash of the commit.
        :type commit: str
        :param tagPushedId: The id of the request event.
        :type tagPushedId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            change, commit, tagPushedId, reconstructedId, reconstructedPreviousEventIds
        )
