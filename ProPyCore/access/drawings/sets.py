from ..base import Base
from ...exceptions import NotFoundItemError

class Sets(Base):
    def __init__(self, access_token, server_url) -> None:
        super().__init__(access_token, server_url)

        self.endpoint = "/rest/v1.0"

    def get(self, company_id, project_id, per_page=100):
        """
        Gets all the available drawing sets

        Parameters
        ----------
        company_id : int
            unique identifier for the company
        project_id : int
            unique identifier for the project
        per_page : int, default 100
            number of drawing sets to include per page

        Returns
        -------
        drawing_sets : list
            available drawing sets data
        """
        headers = {
            "Procore-Company-Id": f"{company_id}"
        }
        
        n_sets = 1
        page = 1
        drawing_sets = []
        
        while n_sets > 0:
            params = {
                "page": page,
                "per_page": per_page
            }

            set_selection = self.get_request(
                api_url=f"{self.endpoint}/projects/{project_id}/drawing_sets",
                additional_headers=headers,
                params=params
            )

            n_sets = len(set_selection)
            drawing_sets += set_selection
            page += 1

        return drawing_sets
