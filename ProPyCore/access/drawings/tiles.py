from ..base import Base

class Tiles(Base):
    def __init__(self, access_token, server_url) -> None:
        super().__init__(access_token, server_url)

        self.endpoint = "/rest/v1.0"

    def get(self, company_id, project_id, drawing_revision_id, page=1, per_page=100):
        """
        Gets all the available drawing tiles for a specific drawing revision

        Parameters
        ----------
        company_id : int
            unique identifier for the company
        project_id : int
            unique identifier for the project
        drawing_revision_id : int
            unique identifier for the drawing revision
        page : int, default 1
            page number
        per_page : int, default 100
            number of drawing tiles to include per page

        Returns
        -------
        drawing_tiles : list
            available drawing tiles data
        """
        headers = {
            "Procore-Company-Id": f"{company_id}"
        }
        
        params = {
            "project_id": project_id,
            "page": page,
            "per_page": per_page
        }

        drawing_tiles = self.get_request(
            api_url=f"{self.endpoint}/projects/{project_id}/drawing_revisions/{drawing_revision_id}/drawing_tiles",
            additional_headers=headers,
            params=params
        )

        return drawing_tiles
