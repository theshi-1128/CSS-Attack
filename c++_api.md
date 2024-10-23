介绍

与 SQLite 和 Noe4j 类似，TuGraph 可以在嵌入式模式下工作。 在嵌入式模式下，它就像一个库。 您可以编写自己的应用程序并调用库函数来创建、查询和修改图。 在这种情况下，应用程序和图数据库之间的所有数据交换都在同一个进程中进行。 它非常简单高效。

这是 TuGraph 嵌入模式的 python API 文档。 通过嵌入式API，用户可以打开或创建数据库，然后查询或修改数据库。

接口

classliblgraph_python_api.AccessLevel
    Access that a user has on a graph.
    Members:
        NONE
        READ
        WRITE
        FULL
    property name

class liblgraph_python_api.EdgeUid
    Edge identifier.
    property dst
        Destination vertex ID.
    property eid
        ID of the edge.
    property lid
        Label ID of the edge.
    property src
        Source vertex ID.
    property tid
        Temporal ID of the edge.
    
class liblgraph_python_api.FieldData
    FieldData is the data type of field value.
    AsBlob(self: liblgraph_python_api.FieldData)→ bytes
        Get value as double, throws exception on type mismatch
    AsBool(self: liblgraph_python_api.FieldData)→ bool
        Get value as bool, throws exception on type mismatch
    AsDate(self: liblgraph_python_api.FieldData)→ datetime.datetime
        Get value as date, throws exception on type mismatch
    AsDateTime(self: liblgraph_python_api.FieldData)→ datetime.datetime
        Get value as datetime, throws exception on type mismatch
    AsDouble(self: liblgraph_python_api.FieldData)→ float
        Get value as double, throws exception on type mismatch
    AsFloat(self: liblgraph_python_api.FieldData)→ float
        Get value as float, throws exception on type mismatch
    AsInt16(self: liblgraph_python_api.FieldData)→ int
        Get value as int16, throws exception on type mismatch
    AsInt32(self: liblgraph_python_api.FieldData)→ int
        Get value as int32, throws exception on type mismatch
    AsInt64(self: liblgraph_python_api.FieldData)→ int
        Get value as int64, throws exception on type mismatch
    AsInt8(self: liblgraph_python_api.FieldData)→ int
        Get value as int8, throws exception on type mismatch
    AsString(self: liblgraph_python_api.FieldData)→ str
        Get value as string, throws exception on type mismatch
    static Blob(arg0: bytes)→ liblgraph_python_api.FieldData
        Make a BLOB value
    static Bool(arg0: bool)→ liblgraph_python_api.FieldData
        Make a BOOL value
    static Date(*args, **kwargs)
        Overloaded function.
        1.Date(arg0: str) -> liblgraph_python_api.FieldData
            Make a DATE value
        2.Date(arg0: datetime.datetime) -> liblgraph_python_api.FieldData
            Make a DATE value
    static DateTime(*args, **kwargs)
        Overloaded function.
        1.DateTime(arg0: str) -> liblgraph_python_api.FieldData
            Make a DATETIME value
        2.DateTime(arg0: datetime.datetime) -> liblgraph_python_api.FieldData
            Make a DATETIME value
    static Double(arg0: float)→ liblgraph_python_api.FieldData
        Make a DOUBLE value
    static Float(arg0: float)→ liblgraph_python_api.FieldData
        Make a FLOAT value
    static Int16(arg0: int)→ liblgraph_python_api.FieldData
        Make a INT16 value
    static Int32(arg0: int)→ liblgraph_python_api.FieldData
        Make a INT32 value
    static Int64(arg0: int)→ liblgraph_python_api.FieldData
        Make a INT64 value
    static Int8(arg0: int)→ liblgraph_python_api.FieldData
        Make a INT8 value
    static String(arg0: str)→ liblgraph_python_api.FieldData
        Make a STRING value
    ToPython(self: liblgraph_python_api.FieldData)→ object
        Convert to corresponding Python type.
    get(self: liblgraph_python_api.FieldData)→ object
    isNull(self: liblgraph_python_api.FieldData)→ bool
    set(self: liblgraph_python_api.FieldData, arg0: object)→ None
    
class liblgraph_python_api.FieldSpec
    Field specification.
    property name
        Name of this field.
    property nullable
        Whether this field can be null.
    property type
        Type of this field, INT8, INT16, …, FLOAT, DOUBLE, STRING.
    
class liblgraph_python_api.FieldType
    Data type of FieldData.
    Members:
        NUL
        BOOL
        INT8
        INT16
        INT32
        INT64
        FLOAT
        DOUBLE
        DATE
        DATETIME
        STRING
        BLOB
    property name
    
class liblgraph_python_api.Galaxy
    A galaxy is a TuGraph instance that holds multiple GraphDBs. A galaxy is stored in a directory and manages users and GraphDBs. Each (user, GraphDB) pair can have different access levels. You can use db=Galaxy.OpenGraph(graph) to open a graph. Since garbage collection in Python is automatic, you need to close the galaxy with Galaxy.Close() when you are done with it.
    Close(self: liblgraph_python_api.Galaxy)→ None
        Closes this galaxy
    CreateGraph(self: liblgraph_python_api.Galaxy, name: str, description: str = '', max_size: int = 4398046511104)→ bool
        Creates a graph. name: the name of the graph description: description of the graph max_size: maximum size of the graph, default 1TB
    CreateRole(self: liblgraph_python_api.Galaxy, name: str, desc: str)→ bool
        Create a role. name: name of the role desc: description of the role
    CreateUser(self: liblgraph_python_api.Galaxy, name: str, password: str, desc: str)→ bool
        Creates a new user account. name: name of the user password: password for the user desc: description of this user
    DeleteGraph(self: liblgraph_python_api.Galaxy, arg0: str)→ bool
        Deletes a graph
    DeleteRole(self: liblgraph_python_api.Galaxy, arg0: str)→ bool
        Deletes the specified role
    DeleteUser(self: liblgraph_python_api.Galaxy, arg0: str)→ bool
        Deletes a user account
    DisableUser(self: liblgraph_python_api.Galaxy, arg0: str)→ bool
        Disables a user
    EnableUser(self: liblgraph_python_api.Galaxy, arg0: str)→ bool
        Enables a user
    GetUserInfo(self: liblgraph_python_api.Galaxy, arg0: str)→ lgraph_api::UserInfo
        Get information of the specified user
    ListGraphs(self: liblgraph_python_api.Galaxy)→ Dict[str, Tuple[str, int]]
        Lists graphs and returns a dictionary of {name:(desc, max_size)}
    ListUsers(self: liblgraph_python_api.Galaxy)→ Dict[str, lgraph_api::UserInfo]
        Lists all users and whether they are admin
    ModGraph(self: liblgraph_python_api.Galaxy, graph_name: str, mod_desc: bool, description: str, mod_size: bool, new_max_size: int)→ bool
        mod_size: whether to modify max graph size new_max_size: new maximum size of the graph, in bytes
    OpenGraph(self: liblgraph_python_api.Galaxy, graph: str, read_only: bool = False)→ lgraph_api::GraphDB
        Opens a graph and returns a GraphDB instance. graph: name of the graph read_only: whether to open the graph in read-only mode
    SetCurrentUser(self: liblgraph_python_api.Galaxy, user: str, password: str)→ None
        Validate user password and set current user. user: user name password: password of the user
    SetRoleAccessRights(self: liblgraph_python_api.Galaxy, arg0: str, arg1: Dict[str, liblgraph_python_api.AccessLevel])→ bool
        Set access rights for the specified role
    SetRoleAccessRightsIncremental(self: liblgraph_python_api.Galaxy, arg0: str, arg1: Dict[str, liblgraph_python_api.AccessLevel])→ bool
        Set access rights for the specified role, only affects the specified graphs
    SetRoleDesc(self: liblgraph_python_api.Galaxy, name: str, desc: str)→ bool
        Set description of the specified role. name: name of the role desc: description of the role
    SetUser(self: liblgraph_python_api.Galaxy, user: str)→ None
        Validate the given user and set current user given in the user.
    SetUserGraphAccess(self: liblgraph_python_api.Galaxy, user: str, graph: str, access: liblgraph_python_api.AccessLevel)→ bool
        Set the access level of the specified user on the graph. user: name of the user graph: name of the graph access: access level of the user on that graph
    SetUserPass(self: liblgraph_python_api.Galaxy, name: str, old_password: str = '', new_password: str)→ bool
        Modifies user password. name: name of the user old_password: current password, not needed when modifying another user new_password: new password for the user
    SetUserRoles(self: liblgraph_python_api.Galaxy, name: str, roles: List[str])→ bool
        Set the roles for the specified user. name: name of the user roles: list of roles for this user
        
class liblgraph_python_api.GraphDB
    The graph database class. A GraphDB stores the data about the graph, including labels, vertices, edges and indexes.Since Garbage Collection in Python is automatic, you need to close the DB with GraphDB.Close() at the end of its lifetime.Make sure you have either committed or aborted every transaction that is using the DB before you close the DB.
    AddEdgeLabel(self: liblgraph_python_api.GraphDB, label_name: str, field_specs: List[liblgraph_python_api.FieldSpec], temporal_field: str = '', constraints: List[Tuple[str, str]] = [])→ bool
        Adds an edge label.
    AddVertexIndex(self: liblgraph_python_api.GraphDB, label_name: str, field_name: str, is_unique: bool)→ bool
        Adds an index.
    AddVertexLabel(self: liblgraph_python_api.GraphDB, label_name: str, field_specs: List[liblgraph_python_api.FieldSpec], primary_field: str)→ bool
        Add a vertex label.
    AlterEdgeLabelAddFields(self: liblgraph_python_api.GraphDB, label: str, add_fields: List[liblgraph_python_api.FieldSpec], default_values: List[liblgraph_python_api.FieldData])→ int
        Add fields to an edge label label: name of the label add_fields: list of FieldSpec for the newly added fields default_values: default values of the added fields
    AlterEdgeLabelDelFields(self: liblgraph_python_api.GraphDB, label: str, del_fields: List[str])→ int
        Delete fields from an edge label label: name of the label del_fields: list of field names
    AlterEdgeLabelModFields(self: liblgraph_python_api.GraphDB, label: str, mod_fields: List[liblgraph_python_api.FieldSpec])→ int
        Modify fields in an edge label label: name of the label mod_fields: list of FieldSpec for the modified fields
    AlterEdgeLabelModifyConstraints(self: liblgraph_python_api.GraphDB, label_name: str, constraints: List[Tuple[str, str]])→ bool
        Modify edge constraints
    AlterVertexLabelAddFields(self: liblgraph_python_api.GraphDB, label: str, add_fields: List[liblgraph_python_api.FieldSpec], default_values: List[liblgraph_python_api.FieldData])→ int
        Add fields to a vertex label label: name of the label add_fields: list of FieldSpec for the newly added fields default_values: default values of the added fields
    AlterVertexLabelDelFields(self: liblgraph_python_api.GraphDB, label: str, del_fields: List[str])→ int
        Delete fields from a vertex label label: name of the label del_fields: list of field names
    AlterVertexLabelModFields(self: liblgraph_python_api.GraphDB, label: str, mod_fields: List[liblgraph_python_api.FieldSpec])→ int
        Modify fields in a vertex label label: name of the label mod_fields: list of FieldSpec for the modified fields
    Close(self: liblgraph_python_api.GraphDB)→ None
        Closes the DB.
    CreateReadTxn(self: liblgraph_python_api.GraphDB)→ lgraph_api::TransactionCreateWriteTxn(self: liblgraph_python_api.GraphDB, optimistic: bool = False)→ lgraph_api::Transaction
        Create a write transaction.
    DeleteEdgeLabel(self: liblgraph_python_api.GraphDB, label_name: str)→ int
        Deletes an edge label
    DeleteVertexIndex(self: liblgraph_python_api.GraphDB, label_name: str, field_name: str)→ bool
        Deletes the specified index.
    DeleteVertexLabel(self: liblgraph_python_api.GraphDB, label_name: str)→ int
        Deletes a vertex label
    DropAllData(self: liblgraph_python_api.GraphDB)→ None
        Drop all the data in this DB. All vertices, edges, labels and indexes will be dropped.
    DropAllVertex(self: liblgraph_python_api.GraphDB)→ None
        Drops all the vertices and edges in this DB. Labels and indexes (though index contents will be cleared due to deletion of vertices) will be preserved.
    EstimateNumVertices(self: liblgraph_python_api.GraphDB)→ int
        Gets an estimation of the number of vertices. This can be inaccurate if there were vertex removals.
    Flush(self: liblgraph_python_api.GraphDB)→ None
        Flushes written data into disk.
    GetDescription(self: liblgraph_python_api.GraphDB)→ str
        Gets description of the graph.
    GetMaxSize(self: liblgraph_python_api.GraphDB)→ int
        Gets maximum size of the graph.
    IsVertexIndexed(self: liblgraph_python_api.GraphDB, label_name: str, field_name: str)→ bool
        Tells whether the specified field is indexed.
        
class liblgraph_python_api.InEdgeIterator
    InEdgeIterator can be used to iterate through all the incoming edges of the destination vertex. Incoming edges are sorted in (dst, label, src, eid) order.
    Delete(self: liblgraph_python_api.InEdgeIterator)→ None
        Deletes current edge. The iterator will point to the next out edge if there is any.
    GetAllFields(self: liblgraph_python_api.InEdgeIterator)→ dict
        Gets all the field values and return as a dict.
    GetDst(self: liblgraph_python_api.InEdgeIterator)→ int
        Returns the id of the destination vertex.
    GetEdgeId(self: liblgraph_python_api.InEdgeIterator)→ int
        Returns the id of current edge. Edge id is unique across the same (src, dst) set.
    GetField(*args, **kwargs)
        Overloaded function.
        1.GetField(self: liblgraph_python_api.InEdgeIterator, field_name: str) -> object
            Gets the field value of the field specified by field_name.
        2.GetField(self: liblgraph_python_api.InEdgeIterator, field_id: int) -> object
            Gets the field value of the field specified by field_id.
    GetFields(*args, **kwargs)
        Overloaded function.
        1.GetFields(self: liblgraph_python_api.InEdgeIterator, field_names: List[str]) -> list
            Gets field values of the fields specified by field_names.
        2.GetFields(self: liblgraph_python_api.InEdgeIterator, field_ids: List[int]) -> list
            Gets field values of the fields specified by field_ids.
    GetLabel(self: liblgraph_python_api.InEdgeIterator)→ str
        Returns the name of the edge label.
    GetLabelId(self: liblgraph_python_api.InEdgeIterator)→ int
        Returns the id of the edge label.
    GetSrc(self: liblgraph_python_api.InEdgeIterator)→ int
        Returns the id of the source vertex.
    GetUid(self: liblgraph_python_api.InEdgeIterator)→ liblgraph_python_api.EdgeUid
        Returns the EdgeUid of the edge.
    Goto(self: liblgraph_python_api.InEdgeIterator, euid: liblgraph_python_api.EdgeUid, nearest: bool)→ bool
        Goes to the in edge specified by euid.
    IsValid(self: liblgraph_python_api.InEdgeIterator)→ bool
        Tells whether the iterator is valid.
    Next(self: liblgraph_python_api.InEdgeIterator)→ bool
        Goes to the next in edge to current destination vertex. If there is no more in edge left, the iterator becomes invalid.
    SetField(self: liblgraph_python_api.InEdgeIterator, field_name: str, field_value_object: object)→ None
        Sets the specified field
    SetFields(*args, **kwargs)
        Overloaded function.
        1.SetFields(self: liblgraph_python_api.InEdgeIterator, field_names: List[str], field_value_strings: List[str]) -> None
            Sets the fields specified by field_names with field values in string representation. field_names specifies the names of the fields to set. field_value_strings are the field values in string representation.
        2.SetFields(self: liblgraph_python_api.InEdgeIterator, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_names with new values. field_names specifies the names of the fields to set. field_values are the FieldData containing field values.
        3.SetFields(self: liblgraph_python_api.InEdgeIterator, value_dict: dict) -> None
            Sets the fields with values as specified in value_dict. value_dict specifies the field_name:value dict.
        4.SetFields(self: liblgraph_python_api.InEdgeIterator, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_ids with field values. field_ids specifies the ids of the fields to set. field_values are the field values to be set.
    ToString(self: liblgraph_python_api.InEdgeIterator)→ str
        Returns the string representation of current edge.

class liblgraph_python_api.IndexSpec
    Index specification.
    property field
        Name of the field
    property label
        Name of the label.
    property unique
        Whether the indexed values are unique.

class liblgraph_python_api.LGraphType
    Members:
    NUL : NUL
    INTEGER : INTEGER
    FLOAT : FLOAT
    DOUBLE : DOUBLE
    BOOLEAN : BOOLEAN
    STRING : STRING
    NODE : NODE
    RELATIONSHIP : RELATIONSHIP
    PATH : PATH
    LIST : LIST
    MAP : MAP
    ANY : ANY
    property name
    
class liblgraph_python_api.OutEdgeIterator
    OutEdgeIterator can be used to iterate through all the out-going edges of the source vertex. Out-going edges are sorted in (src, lid, dst, eid) order.
    Delete(self: liblgraph_python_api.OutEdgeIterator)→ None
        Deletes current edge. The iterator will point to the next out edge if there is any.
    GetAllFields(self: liblgraph_python_api.OutEdgeIterator)→ dict
        Gets all the field values and return as a dict.
    GetDst(self: liblgraph_python_api.OutEdgeIterator)→ int
        Returns the id of the destination vertex.
    GetEdgeId(self: liblgraph_python_api.OutEdgeIterator)→ int
        Returns the id of current edge. Edge id is unique across the same (src, dst) set.
    GetField(*args, **kwargs)
        Overloaded function.
        1.GetField(self: liblgraph_python_api.OutEdgeIterator, field_name: str) -> object
            Gets the field value of the field specified by field_name.
        2.GetField(self: liblgraph_python_api.OutEdgeIterator, field_id: int) -> object
            Gets the field value of the field specified by field_id.
    GetFields(*args, **kwargs)
        Overloaded function.
        1.GetFields(self: liblgraph_python_api.OutEdgeIterator, field_names: List[str]) -> list
            Gets field values of the fields specified by field_names.
        2.GetFields(self: liblgraph_python_api.OutEdgeIterator, field_ids: List[int]) -> list
            Gets field values of the fields specified by field_ids.
    GetLabel(self: liblgraph_python_api.OutEdgeIterator)→ str
        Returns the name of the edge label.
    GetLabelId(self: liblgraph_python_api.OutEdgeIterator)→ int
        Returns the id of the edge label.
    GetSrc(self: liblgraph_python_api.OutEdgeIterator)→ int
        Returns the id of the source vertex.
    GetUid(self: liblgraph_python_api.OutEdgeIterator)→ liblgraph_python_api.EdgeUid
        Returns the EdgeUid of the edge.
    Goto(self: liblgraph_python_api.OutEdgeIterator, euid: liblgraph_python_api.EdgeUid, nearest: bool = False)→ bool
        Goes to the out edge specified by euid.
    IsValid(self: liblgraph_python_api.OutEdgeIterator)→ bool
        Tells whether the iterator is valid.
    Next(self: liblgraph_python_api.OutEdgeIterator)→ bool
        Goes to the next out edge from current source vertex. If there is no more out edge left, the iterator becomes invalid.
    SetField(self: liblgraph_python_api.OutEdgeIterator, field_name: str, field_value_object: object)→ None
        Sets the specified field
    SetFields(*args, **kwargs)
        Overloaded function.
        1.SetFields(self: liblgraph_python_api.OutEdgeIterator, field_names: List[str], field_value_strings: List[str]) -> None
            Sets the fields specified by field_names with field values in string representation. field_names specifies the names of the fields to set. field_value_strings are the field values in string representation.
        2.SetFields(self: liblgraph_python_api.OutEdgeIterator, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_names with field values in string representation. field_names specifies the names of the fields to set. field_values are FieldData containing the field values.
        3.SetFields(self: liblgraph_python_api.OutEdgeIterator, value_dict: dict) -> None
            Sets the field values as specified in value_dict. value_dict specifies the field_name:value dictionary.
        4.SetFields(self: liblgraph_python_api.OutEdgeIterator, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_ids with field values. field_ids specifies the ids of the fields to set. field_values are the field values to be set.
    ToString(self: liblgraph_python_api.OutEdgeIterator)→ str
        Returns the string representation of current edge.

class liblgraph_python_api.PluginErrorCode
    ErrorCode of plugin.
    Members:
        SUCCESS
        INPUT_ERR
        INTERNAL_ERR
        SUCCESS_WITH_SIGNATURE
    property name
    
class liblgraph_python_api.Transaction
    In embedded mode, all the operations are performed in transactions and thus enjoys the power of transactions such as atomicity and isolation. You can commit or abort a transaction at any time without worrying about the side effects it has already made. Transactions can be either committed or aborted, after which it is destructed and becomes invalid. Make sure you have destructed every transaction before you closes the corresponding GraphDB. Transactions also track the created iterators and releases all the iterators during destruction.
    Abort(self: liblgraph_python_api.Transaction)→ NoneAddEdge(*args, **kwargs)
        Overloaded function.
        1.AddEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, field_names: List[str], field_value_strings: List[str]) -> liblgraph_python_api.EdgeUid
            Adds an edge from src to dst with the specified label name, field names, and field values in string format. Returns the id of the newly added edge. Fields that are not in field_names are considered null.
        2.AddEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> liblgraph_python_api.EdgeUid
            Adds an edge from src to dst with the specified label name, field names, and field values. Returns the id of the newly added edge. Fields that are not in field_names are considered null.
        3.AddEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_id: int, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> liblgraph_python_api.EdgeUid
            Adds an edge from src to dst with the specified label id, field ids, and field values. Returns the id of the newly added edge. Fields that are not in field_names are considered null.
        4.AddEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, value_dict: dict) -> liblgraph_python_api.EdgeUid
            Adds an edge from src to dst with the specified label, and fill it with the values given in value_dict. Returns the id of the newly added edge. Fields that are not in value_dict are considered null.
    AddVertex(*args, **kwargs)
        Overloaded function.
        1.AddVertex(self: liblgraph_python_api.Transaction, label_name: str, field_names: List[str], field_value_strings: List[str]) -> int
            Adds a vertex with the specified label name, field names, and field values in string format. Returns the id of the newly added vertex. Fields that are not in field_names are considered null.
        2.AddVertex(self: liblgraph_python_api.Transaction, label_name: str, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> int
            Adds a vertex with the specified label name, field names, and field values. Returns the id of the newly added vertex. Fields that are not in field_names are considered null.
        3.AddVertex(self: liblgraph_python_api.Transaction, label_id: int, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> int
            Adds a vertex with the specified label ids, field ids, and field values. Returns the id of the newly added vertex. Fields that are not in field_ids are considered null.
        4.AddVertex(self: liblgraph_python_api.Transaction, label_name: str, value_dict: dict) -> int
            Adds a vertex with the specified label name and set the value as specified in value_dict. Returns the id of the newly added vertex. Fields that are not specified in the dict are considered null.
    Commit(self: liblgraph_python_api.Transaction)→ NoneDumpGraph(self: liblgraph_python_api.Transaction)→ None
        Prints the string representation of the WHOLE graph to stdout.
    GetEdgeFieldId(*args, **kwargs)
        Overloaded function.
        1.GetEdgeFieldId(self: liblgraph_python_api.Transaction, label_id: int, field_name: str) -> int
            Gets the edge field id associated with this (label_id, field_name). GraphDB assigns integer ids to each field of the same label. Using field id instead of field name can have performance benefits.
        2.GetEdgeFieldId(self: liblgraph_python_api.Transaction, label_id: int, field_names: List[str]) -> List[int]
            Gets the edge field ids associated with this (label_id, field_names). GraphDB assigns integer ids to each field of the same label. Using field id instead of field name can have performance benefits.
    GetEdgeLabelId(self: liblgraph_python_api.Transaction, label_name: str)→ int
        Gets the edge label id associated with this label. GraphDB assigns integer ids to each label. Using label id instead of label name can have performance benefits.
    GetEdgeSchema(self: liblgraph_python_api.Transaction, label_name: str)→ List[liblgraph_python_api.FieldSpec]
        Gets the schema specification of the edge label.
    GetInEdgeIterator(*args, **kwargs)
        Overloaded function.
        1.GetInEdgeIterator(self: liblgraph_python_api.Transaction, euid: liblgraph_python_api.EdgeUid, nearest: bool) -> lgraph_api::InEdgeIterator
            Gets an InEdgeIterator pointing to the in-edge of vertex dst with EdgeUid==euid.
        2.GetInEdgeIterator(self: liblgraph_python_api.Transaction, src: int, dst: int, label_id: int) -> lgraph_api::InEdgeIterator
            Gets an InEdgeIterator from src to dst with label specified by label_id.
    GetNumEdgeLabels(self: liblgraph_python_api.Transaction)→ intGetNumVertexLabels(self: liblgraph_python_api.Transaction)→ intGetOutEdgeIterator(*args, **kwargs)
        Overloaded function.
        1.GetOutEdgeIterator(self: liblgraph_python_api.Transaction, euid: liblgraph_python_api.EdgeUid, nearest: bool) -> lgraph_api::OutEdgeIterator
            Gets an OutEdgeIterator pointing to the edge identified by euid.
        2.GetOutEdgeIterator(self: liblgraph_python_api.Transaction, src: int, dst: int, label_id: int) -> lgraph_api::OutEdgeIterator
            Gets an OutEdgeIterator from src to dst with label specified by label_id.
    GetVertexByUniqueIndex(*args, **kwargs)
        Overloaded function.
        1.GetVertexByUniqueIndex(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, field_value_string: str) -> lgraph_api::VertexIterator
            Gets vertex iterator by unique index. Throws exception if there is no such vertex. label_name specifies the name of the indexed label. field_name specifies the name of the indexed field. field_value_string specifies the string representation of the indexed field value.
        2.GetVertexByUniqueIndex(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, field_value: object) -> lgraph_api::VertexIterator
            Gets vertex iterator by unique index. Throws exception if there is no such vertex. label_name specifies the name of the indexed label. field_name specifies the name of the indexed field. field_value specifies the indexed field value.
        3.GetVertexByUniqueIndex(self: liblgraph_python_api.Transaction, label_id: int, field_id: int, field_value: liblgraph_python_api.FieldData) -> lgraph_api::VertexIterator
            Gets vertex iterator by unique index. Throws exception if there is no such vertex. label_id specifies the id of the indexed label. field_id specifies the id of the indexed field. field_value is a FieldData specifying the indexed field value.
    GetVertexFieldId(self: liblgraph_python_api.Transaction, label_id: int, field_name: str)→ int
        Gets the vertex field id associated with this (label_id, field_name). GraphDB assigns integer ids to each field of the same label. Using field id instead of field name can have performance benefits.
    GetVertexFieldIds(self: liblgraph_python_api.Transaction, label_id: int, field_names: List[str])→ List[int]
        Gets the vertex field ids associated with this (label_id, [field_names]). GraphDB assigns integer ids to each field of the same label. Using field id instead of field name can have performance benefits.
    GetVertexIndexIterator(*args, **kwargs)
        Overloaded function.
        1.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_id: int, field_id: int, key_start: liblgraph_python_api.FieldData, key_end: liblgraph_python_api.FieldData) -> lgraph_api::VertexIndexIterator
            Gets an VertexIndexIterator pointing to the indexed item which has index value [key_start, key_end]. key_start=key_end=v returns an iterator pointing to all vertexes that has field value v. label_id specifies the id of the indexed label. field_id specifies the id of the indexed field. key_start is a FieldData containing the minimum indexed value. key_end is a FieldData containing the maximum indexed value.
        2.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_id: int, field_id: int, value: liblgraph_python_api.FieldData) -> lgraph_api::VertexIndexIterator
            label_id specifies the id of the indexed label. field_id specifies the id of the indexed field. value is a FieldData containing the indexed value.
        3.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, key_start_string: str, key_end_string: str) -> lgraph_api::VertexIndexIterator
            label_name specifies the name of the indexed label. field_id specifies the name of the indexed field. key_start_string is the string representation of the minimum indexed value. key_end_string is the string representation of the maximum indexed value.
        4.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, key_start: liblgraph_python_api.FieldData, key_end: liblgraph_python_api.FieldData) -> lgraph_api::VertexIndexIterator
            label_name specifies the name of the indexed label. field_id specifies the name of the indexed field. key_start is a FieldData containing the minimum indexed value. key_end is a FieldData containing the maximum indexed value.
        5.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, value_string: str) -> lgraph_api::VertexIndexIterator
            label_name specifies the name of the indexed label. field_id specifies the name of the indexed field. value_string is the string representation of the indexed value.
        6.GetVertexIndexIterator(self: liblgraph_python_api.Transaction, label_name: str, field_name: str, value: liblgraph_python_api.FieldData) -> lgraph_api::VertexIndexIterator
            label_name specifies the name of the indexed label. field_id specifies the name of the indexed field. value is a FieldData containing the indexed value.
    GetVertexIterator(*args, **kwargs)
        Overloaded function.
        1.GetVertexIterator(self: liblgraph_python_api.Transaction) -> lgraph_api::VertexIterator
            Returns a VertexIterator pointing to the first vertex in the graph.
        2.GetVertexIterator(self: liblgraph_python_api.Transaction, vid: int) -> lgraph_api::VertexIterator
            Returns a VertexIterator pointing to the vertex specified by vid.
        3.GetVertexIterator(self: liblgraph_python_api.Transaction, vid: int, nearest: bool) -> lgraph_api::VertexIterator
            Gets VertexIterator with vertex id. If nearest==true, go to the first vertex with id >= vid.
    GetVertexLabelId(self: liblgraph_python_api.Transaction, label_name: str)→ int
        Gets the vertex label id associated with this label. GraphDB assigns integer ids to each label. Using label id instead of label name can have performance benefits.
    GetVertexSchema(self: liblgraph_python_api.Transaction, label_name: str)→ List[liblgraph_python_api.FieldSpec]
        Gets the schema specification of the vertex label.
    IsReadOnly(self: liblgraph_python_api.Transaction)→ boolIsValid(self: liblgraph_python_api.Transaction)→ boolIsVertexIndexed(self: liblgraph_python_api.Transaction, label_name: str, field_name: str)→ bool
        Tells whether the specified field is indexed.
    ListEdgeLabels(self: liblgraph_python_api.Transaction)→ List[str]ListVertexIndexes(self: liblgraph_python_api.Transaction)→ List[liblgraph_python_api.IndexSpec]
        Gets the list of all the vertex indexes in the DB.
    ListVertexLabels(self: liblgraph_python_api.Transaction)→ List[str]UpsertEdge(*args, **kwargs)
        Overloaded function.
        1.UpsertEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, field_names: List[str], field_value_strings: List[str]) -> bool
            Upserts an edge from src to dst with the specified label name, field names, and field values in string format. If an src->dst edge already exists, it is updated with the new value. Otherwise a new edge is created. Returns True if the edge is created, False if the edge is updated. Fields that are not in field_names are considered null.
        2.UpsertEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_id: int, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> bool
            Upserts an edge from src to dst with the specified label id, field ids, and field values. If an src->dst edge already exists, it is updated with the new value. Otherwise a new edge is created. Returns True if the edge is created, False if the edge is updated. Fields that are not in field_names are considered null.
        3.UpsertEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> bool
            Upserts an edge from src to dst with the specified label name, field names, and field values. If an src->dst edge already exists, it is updated with the new value. Otherwise a new edge is created. Returns True if the edge is created, False if the edge is updated. Fields that are not in field_names are considered null.
        4.UpsertEdge(self: liblgraph_python_api.Transaction, src: int, dst: int, label_name: str, value_dict: dict) -> bool
            Upserts an edge from src to dst with the specified label, and fill it with the values given in value_dict. If an src->dst edge already exists, it is updated with the new value. Otherwise a new edge is created. Returns True if the edge is created, False if the edge is updated. Fields that are not in value_dict are considered null.
    VertexToString(self: liblgraph_python_api.Transaction, vid: int)→ str
        Returns the string representation of the vertex specified by vid.

class liblgraph_python_api.VertexIndexIterator
    VertexIndexIterator can be used to retrieve the id of indexed vertices. Vertex ids are sorted in ascending order of (index_value, vertex_id).
    GetIndexValue(self: liblgraph_python_api.VertexIndexIterator)→ liblgraph_python_api.FieldData
        Gets the indexed value. Since vertex ids are sorted in (index_value, vertex_id) order, calling Next() may change the current indexed value.
    GetVid(self: liblgraph_python_api.VertexIndexIterator)→ int
        Gets the id of the vertex currently pointed to.
    IsValid(self: liblgraph_python_api.VertexIndexIterator)→ bool
        Tells whether this iterator is valid.
    Next(self: liblgraph_python_api.VertexIndexIterator)→ bool
        Goes to the next indexed vid. If there is no more vertex within the specified key range, the iterator becomes invalid.

class liblgraph_python_api.VertexIterator
    VertexIterator can be used to retrieve info of a vertex, or to scan through multiple vertices. Vertexes are sorted in ascending order of the their ids.
    Delete(self: liblgraph_python_api.VertexIterator)→ Tuple[int, int]
        Deletes current vertex. The iterator will point to the next vertex if there is any.
    GetAllFields(self: liblgraph_python_api.VertexIterator)→ dict
        Gets all the field values and return as a dict.
    GetField(*args, **kwargs)
        Overloaded function.
        1.GetField(self: liblgraph_python_api.VertexIterator, field_name: str) -> object
            Gets the field value of the field specified by field_name.
        2.GetField(self: liblgraph_python_api.VertexIterator, field_id: int) -> object
            Gets the field value of the field specified by field_id.
    GetFields(*args, **kwargs)
        Overloaded function.
        1.GetFields(self: liblgraph_python_api.VertexIterator, field_names: List[str]) -> list
            Gets the field values of the fields specified by field_names.
        2.GetFields(self: liblgraph_python_api.VertexIterator, field_ids: List[int]) -> list
            Gets the field values of the fields specified by field_ids.
    GetId(self: liblgraph_python_api.VertexIterator)→ int
        Gets the integer id of this vertex. GraphDB assigns an integer id for each vertex.
    GetInEdgeIterator(*args, **kwargs)
        Overloaded function.
        1.GetInEdgeIterator(self: liblgraph_python_api.VertexIterator) -> lgraph_api::InEdgeIterator
            Gets an InEgdeIterator pointing to the first in-coming edge of this edge.
        2.GetInEdgeIterator(self: liblgraph_python_api.VertexIterator, arg0: liblgraph_python_api.EdgeUid, arg1: bool) -> lgraph_api::InEdgeIterator
            Gets an InEgdeIterator pointing to the in-edge of this vertex with EdgeUid==euid.
    GetLabel(self: liblgraph_python_api.VertexIterator)→ str
        Gets the label name of current vertex.
    GetLabelId(self: liblgraph_python_api.VertexIterator)→ int
        Gets the label id of current vertex.
    GetNumInEdges(self: liblgraph_python_api.VertexIterator, n_limit: int = 18446744073709551615)→ Tuple[int, bool]
        Gets the number of in-coming edges of this vertex. n_limit specifies the maximum number of edges to scan. Returns a tuple containing the number of in-edges and a bool value indicating whether the limit is exceeded.
    GetNumOutEdges(self: liblgraph_python_api.VertexIterator, n_limit: int = 18446744073709551615)→ Tuple[int, bool]
        Gets the number of out edges of this vertex. n_limit specifies the maximum number of vids to scan.Returns a tuple containing the number of out-edges and a bool value indicating whether the limit is exceeded.
    GetOutEdgeIterator(*args, **kwargs)
        Overloaded function.
        1.GetOutEdgeIterator(self: liblgraph_python_api.VertexIterator) -> lgraph_api::OutEdgeIterator
            Gets an OutEgdeIterator pointing to the first out-going edge of this edge.
        2.GetOutEdgeIterator(self: liblgraph_python_api.VertexIterator, arg0: liblgraph_python_api.EdgeUid, arg1: bool) -> lgraph_api::OutEdgeIterator
            Gets an OutEgdeIterator pointing to the out-edge of this vertex with EdgeUid==euid.
    Goto(self: liblgraph_python_api.VertexIterator, vid: int, nearest: bool)→ bool
        Goes to the vertex specified by vid. If nearest==true, go to the nearest vertex with id>=vid.
    IsValid(self: liblgraph_python_api.VertexIterator)→ boolListDstVids(self: liblgraph_python_api.VertexIterator, n_limit: int = 18446744073709551615)→ Tuple[List[int], bool]
        Lists all destination vids of the out edges. n_limit specifies the maximum number of vids to return. Returns a tuple containing a list of vids and a bool value indicating whether the limit is exceeded.
    ListSrcVids(self: liblgraph_python_api.VertexIterator, n_limit: int = 18446744073709551615)→ Tuple[List[int], bool]
        Lists all source vids of the in edges. n_limit specifies the maximum number of src vids to return. Returns a tuple containing a list of vids and a bool value indicating whether the limit is exceeded.
    Next(self: liblgraph_python_api.VertexIterator)→ bool
        Goes to the next vertex with id>{current_vid}.
    SetField(self: liblgraph_python_api.VertexIterator, field_name: str, field_value_object: object)→ None
        Sets the specified field
    SetFields(*args, **kwargs)
        Overloaded function.
        1.SetFields(self: liblgraph_python_api.VertexIterator, field_names: List[str], field_value_strings: List[str]) -> None
            Sets the fields specified by field_names with field values in string representation. field_names specifies the names of the fields to set. field_value_strings are the field values in string representation.
        2.SetFields(self: liblgraph_python_api.VertexIterator, field_names: List[str], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_names with new values. field_names specifies the names of the fields to set. field_values are the FieldData containing field values.
        3.SetFields(self: liblgraph_python_api.VertexIterator, value_dict: dict) -> None
            Sets the fields with values as specified in value_dict. value_dict specifies the field_name:value dict.
        4.SetFields(self: liblgraph_python_api.VertexIterator, field_ids: List[int], field_values: List[liblgraph_python_api.FieldData]) -> None
            Sets the fields specified by field_ids with field values. field_ids specifies the ids of the fields to set. field_values are the field values to be set.
    ToString(self: liblgraph_python_api.VertexIterator)→ str
        Returns the string representation of current vertex, including properties and edges.

