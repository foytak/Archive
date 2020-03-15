  query Android_V_49001_getBasicUserInfo  {
  user {
    first_name
    last_name
    preferred_language
    registration_time
    birthdate
    email
    id
    nanodegrees: nanodegrees(is_graduated: false)  {
      ...nodeData
      is_term_based
      is_graduated
      color_scheme
      cohorts {
        id
      }
      hero_image {
        url
      }
      enrollment {
        status
      }
      summary
    }
    graduated_nanodegrees: nanodegrees(is_graduated: true) {
      ...nodeData
      is_term_based
      is_graduated
      color_scheme
      hero_image {
        url
      }
      cohorts {
        id
      }
      summary
    }
    courses: courses(is_graduated: false)   {
      ...nodeData
      summary
    }
    graduated_courses: courses(is_graduated: true)  {
      ...nodeData
      summary
    }
  }
}

fragment nodeData on Node {
  key
  title
  version
  semantic_type
}
