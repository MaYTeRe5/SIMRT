from domain.team import Team


class TeamService:

    def create_team(
        self,
        team_id: str,
        name: str,
        assigned_company_id: str
    ) -> Team:

        return Team(
            id=team_id,
            name=name,
            assigned_company_id=assigned_company_id
        )
