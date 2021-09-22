with unpivoted as (
  {{ 
    dbt_utils.unpivot(
      ref('stg_keyword_extraction'),
      cast_to='variant',
      field_name='keyword',
      value_name='details',
      exclude=[
        'id',
        'author',
        'url',
        'title',
        'selftext'
      ],
      remove = []
    ) 
  }}
)
select

  {{ dbt_utils.surrogate_key(['id', 'keyword']) }}
    as keyword_id,
  id,
  author,
  url,
  title,
  keyword,
  details:category :: text as keyword_category,
  selftext,
  details:substring :: text as match_substring,
  details:start_position :: integer as start_position,
  details:end_position  :: integer as end_position

from unpivoted
where match_substring is not null