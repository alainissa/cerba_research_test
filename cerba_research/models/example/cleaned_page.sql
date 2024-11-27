
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with cleaned_page as (

    select *
    from {{ ref('page') }}
    where title is not null -- we check if the title is not null to verify that the page is valid. we could have taken any other important field.

)

select *
from cleaned_page

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
