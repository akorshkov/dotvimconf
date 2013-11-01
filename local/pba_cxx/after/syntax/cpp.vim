" Additional highlighting for cpp files
" Contains liza-specific keywords

syntax keyword lizaKW  Int Double Str StrStream
syntax keyword lizaKW  TRUE_ASCOMPARISION BOOL_YES BOOL_NO BOOL INT_NULL DOUBLE_NULL STR_NULL
syntax keyword lizaKW  AC_BOOL AC_CODE AC_LTEXT AC_MULTILANGSTRING AC_DATE AC_DATE_HOUR AC_ACOLOR AC_SCURRENCY AC_FILE
syntax keyword lizaKW  ASCursor Project DistinctProject Set Order Fetch rdb ASExpression
syntax keyword lizaKW  IsNull IsNotNull IsEmpty IsNotEmpty
syntax keyword lizaKW  ErrorMessage ItemResult ListResult
syntax keyword lizaKW  AddColumn AppendValues AppendValue AddFooter rout CopyCursor
syntax keyword lizaKW  checkID getEntry addEntry updateEntry removeEntry putEntry
syntax keyword lizaKW  validateID validateAccess validateVendorAccess validateAdminAccess AdminAccountID getCurrID
syntax keyword lizaKW  TRACE_CALL_ARGS TRACE_CALL TARG
syntax keyword lizaKW  ORDBMS READ_ONLY FOR_UPDATE
syntax keyword lizaKW  STLRT Type
syntax keyword lizaKW  Ex Validation InternalError ExternalError

highlight link lizaKW Identifier

syntax keyword boostKW  BOOST_AUTO

highlight link boostKW Identifier
