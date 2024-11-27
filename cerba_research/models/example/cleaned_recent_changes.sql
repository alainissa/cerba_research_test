{{ config(materialized='table') }}

with cleaned_recent_changes as (
    -- we are cleaning the recent changes that are not linked to a page
    select rc.*
    from {{ ref('recent_changes') }} rc
    inner join {{ ref('cleaned_page')}} cp on rc.page_id = cp.pageid -- we are doing an inner join to keep only the changes that have a valid page in the database
)

select *
from cleaned_recent_changes