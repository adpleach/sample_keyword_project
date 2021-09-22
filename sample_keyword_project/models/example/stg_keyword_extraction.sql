{%- set query_results = dbt_utils.get_query_results_as_dict('select keyword, keyword_regex, keyword_category from ' ~ ref('keywords')) -%}

with posts as (
  select * from {{ ref("posts") }}
),

mentions as (
    select

        id,
        author,
        url,
        title,
        selftext,

        {% for k in query_results['KEYWORD'] | list %}
        {%- set regex = query_results['KEYWORD_REGEX'][loop.index-1] %}
        {%- set category = query_results['KEYWORD_CATEGORY'][loop.index-1] %}
        object_construct_keep_null(
            'substring', regexp_substr( selftext, '{{ regex }}', 1, 1, 'i'),
            'category', '{{category}}',
            'start_position', regexp_instr( selftext, '{{ regex }}', 1, 1, 0, 'i'),
            'end_position', regexp_instr( selftext, '{{ regex }}', 1, 1, 1, 'i')
        ) as {{ k | replace(" ","_") | replace("|","_") | lower }} {{ "," if not loop.last}}
       {%- endfor %}

    from posts
)

select * from mentions