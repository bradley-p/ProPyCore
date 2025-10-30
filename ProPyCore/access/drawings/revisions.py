from ..base import Base
from ...exceptions import NotFoundItemError

class Revisions(Base):
    def __init__(self, access_token, server_url) -> None:
        super().__init__(access_token, server_url)

        self.endpoint = "/rest/v1.0"

    def get(self, company_id, project_id, per_page=100):
        """
        Gets all the available drawing revisions

        Parameters
        ----------
        company_id : int
            unique identifier for the company
        project_id : int
            unique identifier for the project
        per_page : int, default 100
            number of drawing revisions to include per page

        Returns
        -------
        drawing_revisions : list
            available drawing revisions data
        """
        headers = {
            "Procore-Company-Id": f"{company_id}"
        }
        
        n_revisions = 1
        page = 1
        drawing_revisions = []
        
        while n_revisions > 0:
            params = {
                "page": page,
                "per_page": per_page
            }

            revision_selection = self.get_request(
                api_url=f"{self.endpoint}/projects/{project_id}/drawing_revisions",
                additional_headers=headers,
                params=params
            )

            n_revisions = len(revision_selection)
            drawing_revisions += revision_selection
            page += 1

        return drawing_revisions

    def show(self, company_id, project_id, drawing_revision_id):
        """
        Shows a specific drawing revision

        Parameters
        ----------
        company_id : int
            unique identifier for the company
        project_id : int
            unique identifier for the project
        drawing_revision_id : int
            unique identifier for the drawing revision

        Returns
        -------
        drawing_revision_info : dict
            specific drawing revision information
        """
        headers = {
            "Procore-Company-Id": f"{company_id}"
        }

        drawing_revision_info = self.get_request(
            api_url=f"{self.endpoint}/projects/{project_id}/drawing_revisions/{drawing_revision_id}",
            additional_headers=headers
        )

        return drawing_revision_info
