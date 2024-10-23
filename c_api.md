C++存储过程接口

base64_encode

Base64 encode and decode. Simple implementation, to be used with BLOB fields. If performance is important, look for an optimized implementation.



namespace lgraph_api

namespace base64

Functions



inline std::string Encode(const char *p, size_t s)

Encodes a string to Base64.



参数

p – The string to encode.



s – Size of the string.



返回

The encoded string.



inline std::string Encode(const std::string &str)

Encodes a string to Base64.



参数

str – The string to decode.



返回

The decoded string.



inline bool TryDecode(const char *p, size_t s, std::string &ret)

Tries to decode a Base64 string.



参数

p – The string to decode.



s – Size of the string.



ret – [out] The decoded string.



返回

True if the string was decoded successfully, false otherwise.



inline bool TryDecode(const std::string &str, std::string &out)

Tries to decode a Base64 string.



参数

str – The string to decode.



out – [out] The decoded string.



返回

True if the string was decoded successfully, false otherwise.



inline std::string Decode(const char *p, size_t s)

Decode a Base64 string and throw exception if fails.



抛出

InputError – Thrown if the string is not a valid Base64 string.



参数

p – The string to decode.



s – Size of the string.



返回

The decoded string.



inline std::string Decode(const std::string &str)

Decode a Base64 string and throw exception if fails.



抛出

InputError – Thrown if the string is not a valid Base64 string.



参数

str – The string to decode.



返回

The decoded string.



lgraph

Defines



LGAPI

namespace lgraph_api

Typedefs



typedef bool GetSignature(SigSpec &sig_spec)

typedef bool Process(lgraph_api::GraphDB &db, const std::string &input, std::string &output)

typedef bool ProcessInTxn(lgraph_api::Transaction &txn, const std::string &input, lgraph_api::Result &output)

lgraph_atomic

Implementation of atomic operations, used in lgraph_traversal.



namespace lgraph_api

Functions



template<class T>

inline bool cas(T *ptr, T oldv, T newv)

template<class T>

inline bool write_min(T *a, T b)

template<class T>

inline bool write_max(T *a, T b)

template<class T>

inline void write_add(T *a, T b)

inline void write_add(uint64_t *a, uint64_t b)

inline void write_add(uint32_t *a, uint32_t b)

inline void write_add(int64_t *a, int64_t b)

inline void write_add(int32_t *a, int32_t b)

template<class T>

inline void write_sub(T *a, T b)

inline void write_sub(uint64_t *a, uint64_t b)

inline void write_sub(uint32_t *a, uint32_t b)

inline void write_sub(int64_t *a, int64_t b)

inline void write_sub(int32_t *a, int32_t b)

lgraph_date_time

Implemnets the DateTime, Date and TimeZone classes.



namespace lgraph_api

Functions



static inline constexpr int32_t MinDaysSinceEpochForDate()

min and max values that Date can hold



static inline constexpr int32_t MaxDaysSinceEpochForDate()

Maximum days since epoch for date



static inline constexpr int64_t MinMicroSecondsSinceEpochForDateTime()

min and max values that Date can hold



static inline constexpr int64_t MaxMicroSecondsSinceEpochForDateTime()

Maximum microseconds since epoch for date time



class Date

#include <lgraph_date_time.h>

Implements the Date class. Range of dates is from 0/1/1 to 12/31/9999.



Public Functions



Date()

Construct a new Date object with the date set to 1970/1/1.



explicit Date(const std::chrono::system_clock::time_point &tp)

Construct a new Date object with date set to the specified time. The time point must be in the range of 0/1/1 to 12/31/9999.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

tp – Time point to set the date to.



explicit Date(const YearMonthDay &ymd)

Construct a new Date object with date set to the specified date. The date must be in the range of 0/1/1 to 12/31/9999.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

ymd – Date in the form of year, month and day.



explicit Date(int32_t days_since_epoch)

Construct a new Date object with date set to an offset from epoch, i.e. the date is set to the specified number of days from epoch. The result date must be in the range of 0/1/1 to 12/31/9999.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

days_since_epoch – Number of days since epoch.



explicit Date(const std::string &str)

Parse date from a YYYY-MM-DD string.



抛出

InputError – if the string is not in the correct format.



参数

str – The string.



YearMonthDay GetYearMonthDay() const noexcept

Returns the current Date in the form of year, month and day.



返回

The year month day.



Date operator+(int days) const

Add a number of days to the Date object.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

days – Number of days to add.



返回

The resulting Date object.



Date &operator+=(int days)

Add a number of days to the current Date object. In case of overflow, current object is not modified.



抛出

OutOfRange – Thrown if the resulting date is out of range.



参数

days – Number of days to add.



返回

Reference to the current date.



Date operator-(int days) const

Subtract a number of days from the Date object.



抛出

OutOfRange – Thrown if the resulting date is out of range.



参数

days – Number of days to subtract.



返回

The resulting Date object.



Date &operator-=(int days)

Subtract a number of days from the current Date object. In case of overflow, current object is not modified.



抛出

OutOfRange – Thrown if the resulting date is out of range.



参数

days – Number of days to subtract.



返回

Reference to the current Date object.



bool operator<(const Date &rhs) const noexcept

bool operator<=(const Date &rhs) const noexcept

bool operator>(const Date &rhs) const noexcept

bool operator>=(const Date &rhs) const noexcept

bool operator==(const Date &rhs) const noexcept

bool operator!=(const Date &rhs) const noexcept

int32_t DaysSinceEpoch() const noexcept

Returns the number of days this date is since epoch.



int32_t GetStorage() const noexcept

Returns the number of days this date is since epoch.



explicit operator int32_t() const noexcept

Returns the number of days this date is since epoch.



std::chrono::system_clock::time_point TimePoint() const noexcept

Returns the timepoint corresponding to this date at 00:00 am.



std::string ToString() const noexcept

Get the string representation of the date in the format of YYYY-MM-DD.



explicit operator DateTime() const noexcept

Get the DateTime object corresponding to 00:00 am on this date.



Public Static Functions



static bool Parse(const std::string &str, Date &d) noexcept

Parse date from YYYY-MM-DD, save value in d.



参数

str – The string.



d – [out] The resulting Date.



返回

True if success, otherwise false.



static size_t Parse(const char *beg, const char *end, Date &d) noexcept

Parse date from YYYY-MM-DD, save value in d.



参数

beg – The beg.



end – The end.



d – [out] The result.



返回

Number of bytes parsed (must be 10), 0 if failed.



static Date Now() noexcept

Returns the current Date.



返回

Current Date in UTC.



static Date LocalNow() noexcept

Returns the current Date in local timezone.



返回

Current Date in local timezone.



Private Members



int32_t days_since_epoch_

The days since epoch



struct YearMonthDay

#include <lgraph_date_time.h>

Structure representing a date in the format of year, month and day.



Public Members



int year

The year, 0-9999



unsigned month

Month, 1-12



unsigned day

Day, 1-31



class DateTime

#include <lgraph_date_time.h>

Implements a DateTime class that holds DateTime in the range of 0000-01-01 00:00:00.000000 to 9999-12-31 23:59:59.999999.



Public Functions



DateTime()

Construct a new DateTime object with date set to the epoch time, i.e., 1970-1-1 00:00:00.



explicit DateTime(const std::chrono::system_clock::time_point &tp)

Construct a new DateTime object with date set to the specified timepoint.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

tp – Timepoint to set the DateTime to.



explicit DateTime(const YMDHMSF &ymdhmsf)

Construct a new DateTime object with date set to the specified date and time given in YMDHMSF.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

ymdhmsf – Date and time to set the DateTime to.



explicit DateTime(int64_t microseconds_since_epoch)

Construct a new DateTime object with date set to specified number of microseconds since epoch.



抛出

OutOfRange – Thrown if the time point is out of range.



参数

microseconds_since_epoch – Number of microseconds since epoch.



explicit DateTime(const std::string &str)

Construct a new DateTime object with date set to the specified date and time given in the form of YYYY-MM-DD HH:MM:SS[.FFFFFF].



抛出

OutOfRange – Thrown if the time point is out of range.



InputError – Thrown if str has invalid format.



参数

str – String representation of the date and time in the form of YYYY-MM-DD HH:MM:SS.



YMDHMSF GetYMDHMSF() const noexcept

Get current DateTime in the form of year, month, day, hour, minute, second, fraction.



返回

The ymdhmsf.



DateTime operator+(int64_t n_microseconds) const

Add a number of microseconds to the DateTime.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



参数

n_microseconds – Number of micorseconds to add.



返回

The resulting DateTime.



DateTime &operator+=(int64_t n_microseconds)

Adds a number of microseconds to the current DateTime object. In case of overflow, the current DateTime object is not modified.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



参数

n_microseconds – Number of microseconds to add.



返回

A reference to current object.



DateTime operator-(int64_t n_microseconds) const

Subtract a number of microseconds from the DateTime.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



参数

n_microseconds – Number of microseconds to subtract.



返回

The resulting DateTime.



DateTime &operator-=(int64_t n_microseconds)

Subtract a number of microseconds from the current DateTime object. In case of overflow, the current DateTime object is not modified.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



参数

n_microseconds – Number of microseconds to subtract.



返回

A reference to current object.



bool operator<(const DateTime &rhs) const noexcept

bool operator<=(const DateTime &rhs) const noexcept

bool operator>(const DateTime &rhs) const noexcept

bool operator>=(const DateTime &rhs) const noexcept

bool operator==(const DateTime &rhs) const noexcept

bool operator!=(const DateTime &rhs) const noexcept

int64_t MicroSecondsSinceEpoch() const noexcept

Get the number of microseconds this DateTime is since epoch.



int64_t GetStorage() const noexcept

Get the number of microseconds this DateTime is since epoch.



explicit operator int64_t() const noexcept

Get the number of microseconds this DateTime is since epoch.



std::chrono::system_clock::time_point TimePoint() const noexcept

Get the timepoint correponding to this DateTime.



std::string ToString() const noexcept

Get string representation of the date and time in the form of YYYY-MM-DD HH:MM:SS.[ffffff]



explicit operator Date() const noexcept

Get the Date object corresponding to this DateTime.



DateTime ConvertToUTC()

Get the UTC time corresponding to this DateTime, assuming current DateTime is a local time.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



返回

Object converted to an UTC.



DateTime ConvertToLocal()

Get the local time corresponding to this DateTime, assuming current DateTime is a UTC time.



抛出

OutOfRange – Thrown if the resulting DateTime is out of range.



返回

Object converted to a local.



Public Static Functions



static bool Parse(const std::string &str, DateTime &d) noexcept

Parse date from YYYY-MM-DD HH:MM:SS(.FFFFFF), save value in d.



参数

str – The string.



d – [out] A DateTime to process.



返回

True if success, otherwise false.



static size_t Parse(const char *beg, const char *end, DateTime &d) noexcept

Parse date from YYYY-MM-DD HH:MM:SS(.FFFFFF), save value in d.



参数

beg – The beg.



end – The end.



d – [inout] A DateTime to process.



返回

Number of bytes parsed (must be 19 or 26), 0 if failed.



static DateTime Now() noexcept

Get current DateTime in UTC.



返回

A DateTime.



static DateTime LocalNow() noexcept

Get current DateTime in local timezone.



返回

A DateTime.



Private Members



int64_t microseconds_since_epoch_

struct YMDHMSF

#include <lgraph_date_time.h>

Representation of a DateTime in year, month, day, hour, minute, second, fraction.



Public Members



int year

The year, 0-9999



unsigned month

The month, 1-12



unsigned day

The day, 1-31



unsigned hour

The hour, 0-23



unsigned minute

The minute, 0-59



unsigned second

The second, 0-59



unsigned fraction

The fraction 000000-999999



class TimeZone

#include <lgraph_date_time.h>

A class that represents a time zone.



Public Functions



explicit TimeZone(int time_diff_hours = 0)

Create a timezone which has time difference with UTC in hours time_diff_hours.



抛出

InvalidParameter – Thrown if time_diff_hours is invalid.



参数

time_diff_hours – (Optional) Difference between local timezone and UTC. Must be > =-10 && <=14. Otherwise the function will throw.



DateTime FromUTC(const DateTime &dt) const

Convert a DateTime from UTC time to this time zone.



抛出

OutOfRange – Thrown if the resulting value is out of range.



参数

dt – DateTime in UTC time.



返回

DateTime in local timezone.



DateTime ToUTC(const DateTime &dt) const

Convert a DateTime from this timezone to UTC time.



抛出

OutOfRange – Thrown if the resulting value is out of range.



参数

dt – DateTime in local timezone.



返回

DateTime in UTC.



int64_t UTCDiffSeconds() const noexcept

Returns diff from UTC in seconds, this is used in Date and DateTime



返回

Number of seconds local timezone is from UTC.



int64_t UTCDiffHours() const noexcept

Returns diff from UTC in hours, this is used in Date and DateTime



返回

Number of hours local timezone is from UTC.



Public Static Functions



static const TimeZone &LocalTimeZone() noexcept

Get local timezone.



返回

A const reference to local timezone.



static void UpdateLocalTimeZone() noexcept

Update local timezone, used only when daylight saving time changes. Daylight saving time may change after LocalTZ was initialized, in which case we need to update it. This function will update all references returned by LocalTimeZone().



Private Members



int64_t time_diff_microseconds_

Private Static Functions



static TimeZone GetLocalTZ()

static TimeZone &LocalTZ()

lgraph_db

namespace lgraph

namespace lgraph_api

Functions



bool ShouldKillThisTask()

Determine if we should kill current task.



返回

True if a KillTask command was issued for this task, either due to user request or timeout.



ThreadContextPtr GetThreadContext()

Gets thread context pointer, which can then be used in ShouldKillThisTask(ctx). Calling ShouldKillThisTask() is equivalent to ShouldKillThisTask(GetThreadContext()). In order to save the cost of GetThreadContext(), you can store the context and use it in ShouldKillThisTask(ctx).



Example: ```c++ ThreadContextPtr ctx = GetThreadContext(); while (HasMoreWorkToDo()) { if (ShouldKillThisTask(ctx)) { break; } DoWork(); } ```



返回

The thread context.



bool ShouldKillThisTask(ThreadContextPtr ctx)

Determine if we should kill the task currently running in the thread identified by ctx.



参数

ctx – The context, as obtained with GetThreadContext.



返回

True if a KillTask command was issued for this task.



Variables



const typedef void * ThreadContextPtr

Defines an alias representing the thread context pointer



class GraphDB

#include <lgraph_db.h>

GraphDB represents a graph instance. In TuGraph, each graph instance has its own schema and access control settings. Accessing a GraphDB without appropriate access rights yields WriteNotAllowed.



A GraphDB becomes invalid if Close() is called, in which case all transactions and iterators associated with that GraphDB become invalid. Further operation on that GraphDB yields InvalidGraphDB.



Public Functions



explicit GraphDB(lgraph::AccessControlledDB *db_with_access_control, bool read_only, bool owns_db = false)

For internal use only. Users should use Galaxy::OpenGraph() to get GraphDB.



GraphDB(GraphDB&&)

GraphDB &operator=(GraphDB&&)

~GraphDB()

void Close()

Close the graph. This will close the graph and release all transactions, iterators associated with the graph. After calling Close(), the graph becomes invalid, and cannot be used anymore.



Transaction CreateReadTxn()

Creates a read transaction.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



返回

The new read transaction.



Transaction CreateWriteTxn(bool optimistic = false)

Creates a write transaction. Write operations can only be performed in write transactions, otherwise exceptions will be thrown. A write transaction can be optimistic. Optimistic transactions can run in parallel and any conflict will be detected during commit. If a transaction conflicts with an ealier one, a TxnConflict will be thrown during commit.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



参数

optimistic – (Optional) True to create an optimistic transaction.



返回

The new write transaction.



Transaction ForkTxn(Transaction &txn)

Forks a read transaction. The resulting read transaction will share the same view as the forked one, meaning that when reads are performed on the same vertex/edge, the results will always be identical, whether they are performed in the original transaction or the forked one. Only read transactions can be forked. Calling ForkTxn() on a write txn causes an InvalidFork to be thrown.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



InvalidFork – Thrown when txn is a write transaction.



参数

txn – [in] The read transaction to be forked.



返回

A new read Transaction that shares the same view with txn.



void Flush()

Flushes buffered data to disk. If there have been some async transactions, there could be data that are written to this graph, but not persisted to disk yet. Calling Flush() will persist the data and prevent data loss in case of system crash.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



void DropAllData()

Drop all the data in the graph, including labels, indexes and vertexes/edges..



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



void DropAllVertex()

Drop all vertex and edges but keep the labels and indexes.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



size_t EstimateNumVertices()

Estimate number of vertices. We don’t maintain the exact number of vertices, but only the next vid. This function actually returns the next vid to be used. So if you have deleted a lot of vertices, the result can be quite different from actual number of vertices.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



返回

Estimated number of vertices.



bool AddVertexLabel(const std::string &label, const std::vector<FieldSpec> &fds, const VertexOptions &options)

Adds a vertex label.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if the schema is illegal.



参数

label – The label name.



fds – The field specifications.



primary_field – The primary field.



返回

True if it succeeds, false if the label already exists.



bool DeleteVertexLabel(const std::string &label, size_t *n_modified = nullptr)

Deletes a vertex label and all the vertices with this label.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



参数

label – The label name.



n_modified – [out] (Optional) If non-null, return the number of deleted vertices.



返回

True if it succeeds, false if the label does not exist.



bool AlterVertexLabelDelFields(const std::string &label, const std::vector<std::string> &del_fields, size_t *n_modified = nullptr)

Deletes fields in a vertex label. This function also updates the vertex data and indices accordingly to make sure the database remains in consistent state.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if field not found, or some fields cannot be deleted.



参数

label – The label name.



del_fields – Labels of the fields to be deleted.



n_modified – [out] (Optional) If non-null, return the number of modified vertices.



返回

True if it succeeds, false if the label does not exist.



bool AlterVertexLabelAddFields(const std::string &label, const std::vector<FieldSpec> &add_fields, const std::vector<FieldData> &default_values, size_t *n_modified = nullptr)

Add fields to a vertex label. The new fields in existing vertices will be filled with default values.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if field already exists.



参数

label – The label name.



add_fields – The add fields.



default_values – The default values of the newly added fields.



n_modified – [out] (Optional) If non-null, return the number of modified vertices.



返回

True if it succeeds, false if the label does not exist.



bool AlterVertexLabelModFields(const std::string &label, const std::vector<FieldSpec> &mod_fields, size_t *n_modified = nullptr)

Modify fields in a vertex label, either chage the data type or optional, or both.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if field not found, or is of incompatible data type.



参数

label – The label name.



mod_fields – The new specification of the modified fields.



n_modified – [out] (Optional) If non-null, return the number of modified vertices.



返回

True if it succeeds, false if the label does not exist.



bool AddEdgeLabel(const std::string &label, const std::vector<FieldSpec> &fds, const EdgeOptions &options)

Add a edge label, specifying its schema. It is allowed to specify edge constrains, too. An edge can be bound to several (source_label, destination_label) pairs, which makes sure this type of edges will only be added between these types of vertices. By default, the constain is empty, meaning that the edge is not restricted.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – if invalid schema (invalid specification, re- definition of the same field, etc.).



参数

label – The label name.



fds – The field specifications.



temporal_field – The temporal field for tid.



edge_constraints – (Optional) The edge constraints. An empty constrain means no restriction.



返回

True if it succeeds, false if label already exists.



bool DeleteEdgeLabel(const std::string &label, size_t *n_modified = nullptr)

Deletes an edge label and all the edges of this type.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



参数

label – The label.



n_modified – [out] (Optional) If non-null, return the number of deleted edges.



返回

True if it succeeds, false if label does not exist.



bool AlterLabelModEdgeConstraints(const std::string &label, const std::vector<std::pair<std::string, std::string>> &constraints)

Modify edge constraint. Existing edges that violate the new constrain will be removed.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if any vertex label does not exist.



参数

label – The label name.



constraints – The new edge constraint.



返回

True if it succeeds, false if the edge label does not exist.



bool AlterEdgeLabelDelFields(const std::string &label, const std::vector<std::string> &del_fields, size_t *n_modified = nullptr)

Deletes fields in an edge label.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if any field does not exist, or cannot be deleted.



参数

label – The label name.



del_fields – The fields to be deleted.



n_modified – [out] (Optional) If non-null, return the number of edges modified.



返回

True if it succeeds, false if it fails.



bool AlterEdgeLabelAddFields(const std::string &label, const std::vector<FieldSpec> &add_fields, const std::vector<FieldData> &default_values, size_t *n_modified = nullptr)

Add fields to an edge label. The new fields in existing edges will be set to default values.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if any field already exists, or the default value is of incompatible type.



参数

label – The label name.



add_fields – The fields to add.



default_values – The default values.



n_modified – [inout] (Optional) If non-null, return the number of modified edges.



返回

True if it succeeds, false if the edge label does not exist.



bool AlterEdgeLabelModFields(const std::string &label, const std::vector<FieldSpec> &mod_fields, size_t *n_modified = nullptr)

Modify fields in an edge label. Data type and OPTIONAL can be modified.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if any field does not exist, or is of incompatible data type.



参数

label – The label name.



mod_fields – The modifier fields.



n_modified – [inout] (Optional) If non-null, return the number of modified edges.



返回

True if it succeeds, false if the label does not exist.



bool AddVertexIndex(const std::string &label, const std::string &field, IndexType type)

Adds an index to ‘label:field’. This function blocks until the index is fully created.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label:field does not exist, or not indexable.



参数

label – The label name.



field – The field name.



is_unique – True if is unique index, false if not.



返回

True if it succeeds, false if the index already exists.



bool AddEdgeIndex(const std::string &label, const std::string &field, IndexType type)

Adds an index to ‘label:field’. This function blocks until the index is fully created.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label:field does not exist, or not indexable.



参数

label – The label.



field – The field.



is_unique – True if the field content is unique for each vertex.



返回

True if it succeeds, false if the index already exists.



bool AddVertexCompositeIndex(const std::string &label, const std::vector<std::string> &fields, CompositeIndexType type)

bool AddVectorIndex(bool is_vertex, const std::string &label, const std::string &field, const std::string &index_type, int vec_dimension, const std::string &distance_type, std::vector<int> &index_spec)

Adds a vector index to ‘label:field’. This function blocks until the index is fully created.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label:field does not exist, or not indexable.



参数

is_vertex – vertex or edge.



label – The label.



field – The field.



is_unique – True if the field content is unique for each vertex.



index_type – Type of the index



vec_dimension – Dimension of the vector



distance_type – Type of the distance



index_spec – Specification of the index



返回

True if it succeeds, false if the index already exists.



bool IsVertexIndexed(const std::string &label, const std::string &field)

Check if this vertex_label:field is indexed.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



InputError – Thrown if label:field does not exist.



参数

label – The label.



field – The field.



返回

True if index exists, false if label:field exists but not indexed.



bool IsEdgeIndexed(const std::string &label, const std::string &field)

Check if this edge_label:field is indexed.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



InputError – Thrown if label:field does not exist.



参数

label – The label.



field – The field.



返回

True if index exists, false if label:field exists but not indexed.



bool IsVertexCompositeIndexed(const std::string &label, const std::vector<std::string> &field)

bool DeleteVertexIndex(const std::string &label, const std::string &field)

Deletes the index to ‘vertex_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label or field does not exist.



参数

label – The label.



field – The field.



返回

True if it succeeds, false if the index does not exists.



bool DeleteVertexCompositeIndex(const std::string &label, const std::vector<std::string> &fields)

bool DeleteEdgeIndex(const std::string &label, const std::string &field)

Deletes the index to ‘edge_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label or field does not exist.



参数

label – The label.



field – The field.



返回

True if it succeeds, false if the index does not exists.



bool DeleteVectorIndex(bool is_vertex, const std::string &label, const std::string &field)

Deletes the vector index to ‘vertex_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if label or field does not exist.



参数

is_vertex – vertex or edge.



label – The label.



field – The field.



返回

True if it succeeds, false if the index does not exists.



std::string GetDescription() const

Get graph description



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



返回

The description.



size_t GetMaxSize() const

Get maximum graph size



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



返回

The maximum size.



bool AddVertexFullTextIndex(const std::string &vertex_label, const std::string &field)

Add fulltext index to ‘vertex_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if vertex label or field does not exist.



参数

vertex_label – The vertex label.



field – The field.



返回

True if it succeeds, false if the fulltext index already exists.



bool AddEdgeFullTextIndex(const std::string &edge_label, const std::string &field)

Add fulltext index to ‘edge_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if edge label or field does not exist.



参数

edge_label – The edge label.



field – The field.



返回

True if it succeeds, false if the fulltext index already exists.



bool DeleteVertexFullTextIndex(const std::string &vertex_label, const std::string &field)

Delete the fulltext index of ‘vertex_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if vertex label or field does not exist.



参数

vertex_label – The vertex label.



field – The field.



返回

True if it succeeds, false if the fulltext index does not exists.



bool DeleteEdgeFullTextIndex(const std::string &edge_label, const std::string &field)

Delete the fulltext index of ‘edge_label:field’



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



InputError – Thrown if edge label or field does not exist.



参数

edge_label – The edge label.



field – The field.



返回

True if it succeeds, false if the fulltext index does not exists.



void RebuildFullTextIndex(const std::set<std::string> &vertex_labels, const std::set<std::string> &edge_labels)

Rebuild the fulltext index of vertex_labels and edge_labels.



参数

vertex_labels – The vertex labels whose fulltext index need to rebuild.



edge_labels – The edge labels whose fulltext index need to rebuild.



std::vector<std::tuple<bool, std::string, std::string>> ListFullTextIndexes()

List fulltext indexes of vertex and edge



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



返回

Format of returned data : (is_vertex, label_name, property_name)



std::vector<std::pair<int64_t, float>> QueryVertexByFullTextIndex(const std::string &label, const std::string &query, int top_n)

Query vertex by fulltext index.



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



InputError – Thrown if label does not exist.



参数

label – The vertex label.



query – Lucene query language.



top_n – return top n data.



返回

Vertex vids and score. Throws exception on error.



std::vector<std::pair<EdgeUid, float>> QueryEdgeByFullTextIndex(const std::string &label, const std::string &query, int top_n)

Query edge by fulltext index



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



InputError – Thrown if label does not exist.



参数

label – The edge label.



query – Lucene query language.



top_n – return top n data.



返回

Edge uids and score. Throws exception on error.



void RefreshCount()

Recount the total number of vertex and edge, stop writing during the count



抛出

InvalidGraphDB – Thrown when currently GraphDB is invalid.



WriteNotAllowed – Thrown when called on a GraphDB with read-only access level.



Private Functions



GraphDB(const GraphDB&) = delete

Copying is disabled.



GraphDB &operator=(const GraphDB&) = delete

Private Members



lgraph::AccessControlledDB *db_

bool should_delete_db_ = false

bool read_only_ = false

lgraph_edge_index_iterator

namespace lgraph

namespace lgraph_api

class EdgeIndexIterator

#include <lgraph_edge_index_iterator.h>

EdgeIndexIterator can be used to access a set of edges that has the same indexed value. If the index is unique (that is, each Edge has a unique index value), then each EdgeIndexIterator will only have one edge unique id, and will become invalid after Next() is called.



An EdgeIndexIterator is valid iff it points to a valid (index_value, euid) pair, otherwise it is invalid. Calling member function on an invalid EdgeIndexIterator throws an exception, except for the IsValid() function.



Public Functions



EdgeIndexIterator(EdgeIndexIterator &&rhs)

EdgeIndexIterator &operator=(EdgeIndexIterator&&)

~EdgeIndexIterator()

void Close()

Closes this iterator



bool IsValid() const

Query if this iterator is valid, i.e. the Key and Vid can be queried.



返回

True if valid, false if not.



bool Next()

Move to the next edge unique id in the list, which consists of all the valid edge unique ids of the iterator and is sorted from small to large. If we hit the end of the list, iterator will become invalid and false is returned.



返回

True if it succeeds, otherwise false.



FieldData GetIndexValue() const

Gets the current index value. The euids are sorted in ( EdgeIndexValue, euid) order. When Next() is called, the iterator moves from one euid to next, possibly moving from one EdgeIndexValue to another. This function tells the EdgeIndexValue currently pointed to.



返回

The key.



EdgeUid GetUid() const

Gets the Edge Unique Id



返回

The UID.



int64_t GetSrc() const

Gets the source vertex id.



返回

The source vertex id.



int64_t GetDst() const

Gets destination of the edge.



返回

The destination vertex id.



size_t GetLabelId() const

Gets label id of this edge.



返回

The label identifier.



int64_t GetEdgeId() const

Gets edge id.



返回

The edge identifier.



Private Functions



EdgeIndexIterator(lgraph::EdgeIndexIterator &&it, const std::shared_ptr<lgraph::Transaction> &txn)

EdgeIndexIterator(const EdgeIndexIterator&) = delete

EdgeIndexIterator &operator=(const EdgeIndexIterator&) = delete

Private Members



std::unique_ptr<lgraph::EdgeIndexIterator> it_

std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class Transaction

lgraph_edge_iterator

namespace lgraph

namespace graph

namespace lgraph_api

Functions



bool operator==(const OutEdgeIterator &lhs, const OutEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator==(const OutEdgeIterator &lhs, const InEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator==(const InEdgeIterator &lhs, const OutEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator==(const InEdgeIterator &lhs, const InEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator!=(const OutEdgeIterator &lhs, const OutEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator!=(const OutEdgeIterator &lhs, const InEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator!=(const InEdgeIterator &lhs, const OutEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



bool operator!=(const InEdgeIterator &lhs, const InEdgeIterator &rhs)

Check whether lhs and rhs points to the same edge.



class InEdgeIterator

#include <lgraph_edge_iterator.h>

An InEdgeIterator can be used to iterate through the in-coming edges of a vertex. Edges are sorted in (lid, tid, src, eid) order, and each (dst, lid, tid, src, eid) tuple is guaranteed to uniquely identify an edge.



An InEdgeIterator is valid iff it points to a valid in-coming edge, otherwise it is invalid. Calling member function on an invalid InEdgeIterator throws an exception, except for the IsValid() and Goto() functions.



The following operations invalidates an InEdgeIterator:



Constructing an InEdgeIterator for non-existing edge.



Calling Goto() with the id of a non-existing edge.



Calling Next() on the last in-coming edge.



Calling Delete() on the last in-coming edge.



Calling Close() on the iterator.



In TuGraph, every iterator belongs to a transaction, and can only be used when the transaction is valid. Calling member functions on an iterator inside an invalid transaction yields InvalidTxn, except for Invalid().



Public Functions



InEdgeIterator(InEdgeIterator &&rhs)

InEdgeIterator &operator=(InEdgeIterator&&)

~InEdgeIterator()

void Close() noexcept

Closes this iterator. The iterator turns invalid after being closed.



bool Next()

Move to the next incoming edge to current destination vertex. If there is no more edge, the iterator becomes invalid and false is returned.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

True if it succeeds, false if it fails.



bool Goto(EdgeUid euid, bool nearest = false)

Go to the edge specified by euid. If the specified edge cannot be found and nearest==true, then try to get the next in-coming edge to the vertex euid.dst, sorted by (label, tid, src, eid). If there is no such edge, iterator is invalidated and false is returned.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



参数

euid – Edge Unique Id.



nearest – (Optional) True to get the nearest edge if the specified one cannot be found.



返回

True if it succeeds, false if it fails.



EdgeUid GetUid() const

Gets the Edge Unique Id



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The UID.



int64_t GetSrc() const

Gets the source vertex id.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The source vertex id.



int64_t GetDst() const

Gets destination vertex id.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The destination vertex id.



int64_t GetEdgeId() const

Gets edge id.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The edge id.



int64_t GetTemporalId() const

Gets temporal id.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The temporal id.



bool IsValid() const

Query if this iterator is valid.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

True if valid, false if not.



const std::string &GetLabel() const

Gets the label of this edge.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The label.



int16_t GetLabelId() const

Gets label id of this edge.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



返回

The label identifier.



std::vector<FieldData> GetFields(const std::vector<std::string> &field_names) const

Gets the fields specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if any field does not exist.



参数

field_names – List of names of the fields.



返回

The fields.



FieldData GetField(const std::string &field_name) const

Gets the field specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if field does not exist.



参数

field_name – Field name.



返回

Field value.



std::vector<FieldData> GetFields(const std::vector<size_t> &field_ids) const

Gets the fields specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if any field does not exist.



参数

field_ids – List of ids for the fields.



返回

The fields.



FieldData GetField(size_t field_id) const

Gets the field specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if field does not exist.



参数

field_id – Field ID.



返回

Field value.



inline FieldData operator[](const std::string &field_name) const

Get field identified by field_name



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if field does not exist.



参数

field_name – Filename of the file.



返回

The indexed value.



inline FieldData operator[](size_t fid) const

Get field identified by field id



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if field does not exist.



参数

fid – The field id.



返回

The indexed value.



std::map<std::string, FieldData> GetAllFields() const

Gets all fields of current vertex.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



InputError – Thrown if any field does not exist.



返回

All field names and values stored as a {(field_name, field_value),…} map.



void SetField(const std::string &field_name, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



InputError – Thrown if any field does not exist.



参数

field_name – Field name.



field_value – Field value.



void SetField(size_t field_id, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



InputError – Thrown if field does not exist.



参数

field_id – Field id.



field_value – Field value.



void SetFields(const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Sets the fields specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



InputError – Thrown if any field does not exist or field value type is incorrect.



参数

field_names – List of names of the fields.



field_value_strings – The field value strings.



void SetFields(const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



InputError – Thrown if any field does not exist or field value type is incorrect.



参数

field_names – List of names of the fields.



field_values – The field values.



void SetFields(const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



InputError – Thrown if any field does not exist or field value type is incorrect.



参数

field_ids – List of identifiers for the fields.



field_values – The field values.



void Delete()

Deletes this edge. The iterator will point to the next incoming edge sorted by (lid, tid, src, eid) if there is any. If no in-coming edge is left for this vertex, the iterator becomes invalid.



抛出

InvalidTxn – Thrown if the transaction is invalid.



InvalidIterator – Thrown if the iterator is invalid.



WriteNotAllowed – Thrown if called inside a read-only transaction.



std::string ToString() const

Get string representation of the edge.



Private Functions



InEdgeIterator(lgraph::graph::InEdgeIterator&&, const std::shared_ptr<lgraph::Transaction>&)

Constructors are private, use Transaction::GetInEdgeIterator() or VertexIterator::GetInEdgeIterator() instead.



InEdgeIterator(const InEdgeIterator&) = delete

InEdgeIterator &operator=(const InEdgeIterator&) = delete

Private Members



std::unique_ptr<lgraph::graph::InEdgeIterator> it_

std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class Transaction

friend class VertexIterator

class OutEdgeIterator

#include <lgraph_edge_iterator.h>

An OutEdgeIterator can be used to iterate through the out-going edges of a vertex. Edges are sorted in (lid, dst, eid) order, and each (src, lid, tid, dst, eid) tuple is guaranteed to uniquely identify an edge.



An OutEdgeIterator is valid iff it points to a valid out-going edge, otherwise it is invalid. Calling member function on an invalid OutEdgeIterator throws an InvalidIterator, except for the IsValid() and Goto() functions.



The following operations invalidates an OutEdgeIterator:



Constructing an OutEdgeIterator for non-existing edge.



Calling Goto() with the id of a non-existing edge.



Calling Next() on the last out-going edge.



Calling Delete() on the last out-going edge.



Calling Close() on the iterator.



In TuGraph, every iterator belongs to a transaction, and can only be used when the transaction is valid. Calling member functions on an iterator inside an invalid transaction yields InvalidTxn, except for Invalid().



Public Functions



OutEdgeIterator(OutEdgeIterator &&rhs)

OutEdgeIterator &operator=(OutEdgeIterator &&rhs)

~OutEdgeIterator()

void Close() noexcept

Closes this iterator. The iterator turns invalid after being closed.



bool Goto(EdgeUid euid, bool nearest = false)

Go to the edge specified by euid. That is, an edge from Vertex euid.src to euid.dst, with LabelId==euid.label, Tid==euid.tid, and EdgeId==euid.eid. If neareast==true and the exact edge was not found, the iterator tries to get the next edge that sorts after the specified edge. The edges are sorted in (label, tid, dst, eid) order. The iterator becomes invalid if there is no outgoing edge from euid.src that sorts after euid.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



参数

euid – Edge Unique ID.



nearest – (Optional) True to get the nearest edge if the specified one cannot be found.



返回

True if it succeeds, false if there is no such edge.



bool IsValid() const noexcept

Query if this iterator is valid.



返回

True if valid, false if not.



bool Next()

Move to the next edge. Invalidates iterator if there is no more out edges from current source vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

True if it succeeds, false if it fails (no more out edge from current source).



EdgeUid GetUid() const

Gets the Edge Unique Id



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The UID.



int64_t GetDst() const

Gets destination of the edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The destination vertex id.



int64_t GetEdgeId() const

Gets edge id.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The edge identifier.



int64_t GetTemporalId() const

Gets primary id.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The primary id of the edge.



int64_t GetSrc() const

Gets the source vertex id.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The source vertex id.



const std::string &GetLabel() const

Gets the label of this edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The label.



int16_t GetLabelId() const

Gets label id of this edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The label identifier.



std::vector<FieldData> GetFields(const std::vector<std::string> &field_names) const

Gets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



返回

The fields.



FieldData GetField(const std::string &field_name) const

Gets the field specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – Field name.



返回

Field value.



std::vector<FieldData> GetFields(const std::vector<size_t> &field_ids) const

Gets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_ids – List of ids for the fields.



返回

The fields.



FieldData GetField(size_t field_id) const

Gets the field specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_id – Field ID.



返回

Field value.



inline FieldData operator[](const std::string &field_name) const

Get field identified by field_name.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – The name of the field to get.



返回

Field value.



inline FieldData operator[](size_t fid) const

Get field identified by field id. FieldId can be obtained with txn.GetEdgeFieldId()



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

fid – fid The field id.



返回

Field value.



std::map<std::string, FieldData> GetAllFields() const

Gets all fields of current vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

All fields in a dictionary of {(field_name, field_value),…}.



void SetField(const std::string &field_name, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – Field name.



field_value – Field value.



void SetField(size_t field_id, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_id – Field id.



field_value – Field value.



void SetFields(const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



field_value_strings – The field value in string representation.



void SetFields(const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



field_values – The field values.



void SetFields(const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_ids – List of identifiers for the fields.



field_values – The field values.



void Delete()

Deletes this edge. The iterator will point to the next out-going edge sorted by (label, tid, dst, eid) if there is any. If there is no more out-going edges for this source vertex, the iterator becomes invalid.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



std::string ToString() const

Get string representation of the edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

A std::string that represents this object.



Private Functions



OutEdgeIterator(lgraph::graph::OutEdgeIterator&&, const std::shared_ptr<lgraph::Transaction>&)

Constructors are private, use Transaction::GetInEdgeIterator() or VertexIterator::GetInEdgeIterator() instead.



OutEdgeIterator(const OutEdgeIterator&) = delete

OutEdgeIterator &operator=(const OutEdgeIterator&) = delete

Private Members



std::unique_ptr<lgraph::graph::OutEdgeIterator> it_

std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class Transaction

friend class VertexIterator

lgraph_exceptions

Defines



ERROR_CODES

X(code, msg)

THROW_CODE(code, ...)

namespace lgraph_api

Enums



enum class ErrorCode

Values:



enumerator X

enumerator ERROR_CODES

Functions



const char *ErrorCodeToString(ErrorCode code)

const char *ErrorCodeDesc(ErrorCode code)

class LgraphException : public exception

#include <lgraph_exceptions.h>

Public Functions



explicit LgraphException(ErrorCode code)

explicit LgraphException(ErrorCode code, const std::string &msg)

explicit LgraphException(ErrorCode code, const char *msg)

template<typename ...Ts>

inline explicit LgraphException(ErrorCode code, const char *format, const Ts&... ds)

inline ErrorCode code() const

inline const std::string &msg() const

inline const char *what() const noexcept override

Private Members



ErrorCode code_

std::string msg_

std::string what_

lgraph_galaxy

namespace lgraph

namespace lgraph_api

class Galaxy

#include <lgraph_galaxy.h>

A galaxy is the storage engine for one TuGraph instance. It manages a set of User/Role/GraphDBs.



A galaxy can be opened in async mode, in which case ALL write transactions will be treated as async, whether they declare async or not. This can come in handy if we are performing a lot of writing, but can cause data loss for online processing.



Public Functions



explicit Galaxy(const std::string &dir, bool durable = false, bool create_if_not_exist = true)

Constructor.



抛出

DBNotExist – Thrown if DB does not exist and create_if_not_exist is false.



IOError – Thrown if DB does not exist, but we failed to create the DB due to IO error.



InputError – Thrown if there are other input errors. e.g., dir is actually a plain file, or DB is corruptted.



参数

dir – The TuGraph dir.



durable – (Optional) True to open in durable mode. If set to false, ALL write transactions are async, whether they declare async or not.



create_if_not_exist – (Optional) If true, the TuGraph DB will be created if dir does not exist; otherwise, an exception is thrown.



Galaxy(const std::string &dir, const std::string &user, const std::string &password, bool durable, bool create_if_not_exist)

Constructor. Open the Galaxy and try to login with specified user and password.



抛出

DBNotExist – Thrown if DB does not exist and create_if_not_exist is false.



IOError – Thrown if DB does not exist, but we failed to create the DB due to IO error.



InputError – Thrown if there are other input errors. e.g., dir is actually a plain file, or DB is corruptted.



Unauthorized – Thrown if user/password is not correct.



参数

dir – The dir.



user – The user.



password – The password.



durable – True to open the Galaxy in durable mode.



create_if_not_exist – True to create if DB does not exist.



Galaxy(Galaxy&&)

Galaxy &operator=(Galaxy&&)

~Galaxy()

void SetCurrentUser(const std::string &user, const std::string &password)

Validate and set current user



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user/password is incorrect.



参数

user – The user.



password – The password.



void SetUser(const std::string &user)

Set current user



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if token is incorrect.



参数

user – The current user.



bool CreateGraph(const std::string &graph_name, const std::string &description = "", size_t max_size = (size_t)1 << 40)

Validate token and set current user



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission to create graph.



InputError – Other input errors such as invalid graph name, size, etc.



参数

graph_name – Name of the graph to create. description (Optional) Description of the graph. max_size (Optional) Maximum size of the graph.



返回

True if it succeeds, false if graph already exists.



bool DeleteGraph(const std::string &graph_name)

Delete a graph



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission to delete graph.



参数

graph_name – Name of the graph.



返回

True if it succeeds, false if the graph does not exist.



bool ModGraph(const std::string &graph_name, bool mod_desc, const std::string &desc, bool mod_size, size_t new_max_size)

Modify graph info



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission to modify graph.



参数

graph_name – Name of the graph.



mod_desc – True to modifier description.



desc – The new description.



mod_size – True to modifier size.



new_max_size – New maximum size.



返回

True if it succeeds, false if it fails.



std::map<std::string, std::pair<std::string, size_t>> ListGraphs() const

List graphs



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission to list graphs.



返回

A dictionary of {graph_name: (description, max_size)}



bool CreateUser(const std::string &user, const std::string &password, const std::string &desc = "")

Creates a user



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if other input errors, such as illegal user name, password, etc.



参数

user – The user.



password – The password.



desc – (Optional) The description.



返回

True if it succeeds, false if user already exists.



bool DeleteUser(const std::string &user)

Deletes the user.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



参数

user – The user.



返回

True if it succeeds, false if user does not exist.



bool SetPassword(const std::string &user, const std::string &old_password, const std::string &new_password)

Set the password of the specified user.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission, or curr_user==user, but old_password is incorrect.



InputError – Thrown if new_password is illegal.



参数

user – The user to modify.



old_password – The old password, required if curr_user==user.



new_password – The new password.



返回

True if it succeeds, false if user does not exist.



bool SetUserDesc(const std::string &user, const std::string &desc)

Sets user description.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if desc is illegal.



参数

user – The user.



desc – The new description.



返回

True if it succeeds, false if user does not exist.



bool SetUserRoles(const std::string &user, const std::vector<std::string> &roles)

Set the roles of the specified user. If you need to add or delete a role, you will need to use GetUserInfo to get the roles first.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if any role does not exist.



参数

user – The user.



roles – A list of roles.



返回

True if it succeeds, false if user does not exist.



bool SetUserGraphAccess(const std::string &user, const std::string &graph, const AccessLevel &access)

Sets user access rights on a graph.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if graph does not exist.



参数

user – The user.



graph – The graph.



access – The access level.



返回

True if it succeeds, false if it user does not exist.



bool DisableUser(const std::string &user)

Disable a user. A disabled user is not able to login or perform any operation. A user cannot disable itself.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if user name is illegal.



参数

user – The user to disable.



返回

True if it succeeds, false if user does not exist.



bool EnableUser(const std::string &user)

Enables the user.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if user name is illegal.



参数

user – The user.



返回

True if it succeeds, false if user does not exist.



std::map<std::string, UserInfo> ListUsers() const

List all users



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



返回

A dictionary of {user_name:user_info}



UserInfo GetUserInfo(const std::string &user) const

Gets user information



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



参数

user – The user.



返回

The user information.



bool CreateRole(const std::string &role, const std::string &desc)

Create a role. A role has different access levels to different graphs. Every user must be assigned some role to get access to graphs.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name or desc is illegal.



参数

role – The role.



desc – The description.



返回

True if it succeeds, false if role already exists.



bool DeleteRole(const std::string &role)

Deletes the role described by role



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name is illegal.



参数

role – The role.



返回

True if it succeeds, false if role does not exist.



bool DisableRole(const std::string &role)

Disable a role. A disabled role still has the data, but is not effective. i.e., users will not have access rights to graphs that are obtained by having this role.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name is illegal.



参数

role – The role.



返回

True if it succeeds, false if the role does not exist.



bool EnableRole(const std::string &role)

Enables the role.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name is illegal.



参数

role – The role.



返回

True if it succeeds, false if role does not exist.



bool SetRoleDesc(const std::string &role, const std::string &desc)

Set the description of the specified role



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name or desc is illegal.



参数

role – The role.



desc – The description.



返回

True if it succeeds, false if role does not exist.



bool SetRoleAccessRights(const std::string &role, const std::map<std::string, AccessLevel> &graph_access)

Set access of the role to graphs. If you need to add or remove access to part of the graphs, you need to get full graph_access map by using GetRoleInfo first.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name or any of the graph name is illegal.



参数

role – The role.



graph_access – The graph access.



返回

True if it succeeds, false if role does not exist.



bool SetRoleAccessRightsIncremental(const std::string &role, const std::map<std::string, AccessLevel> &graph_access)

Incrementally modify the access right of the specified role. For example, for a role that has access right {graph1:READ, graph2:WRITE}, calling this function with graph_access={graph2:READ, graph3:FULL} will set the access right of this role to {graph1:READ, graph2:READ, graph3:FULL}



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name or any of the graph name is illegal.



参数

role – The role.



graph_access – The graph access.



返回

True if it succeeds, false if role does not exist.



RoleInfo GetRoleInfo(const std::string &role) const

Gets role information



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if role name is illegal.



参数

role – The role.



返回

The role information.



std::map<std::string, RoleInfo> ListRoles() const

List all the roles



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



返回

A dictionary of {role_name:RoleInfo}



AccessLevel GetAccessLevel(const std::string &user, const std::string &graph) const

Get the access level that the specified user have to the graph



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if user name or graph name is illegal.



参数

user – The user.



graph – The graph.



返回

The access level.



GraphDB OpenGraph(const std::string &graph, bool read_only = false) const

Opens a graph.



抛出

InvalidGalaxy – Thrown if current galaxy is invalid.



Unauthorized – Thrown if user does not have permission.



InputError – Thrown if graph name is illegal.



参数

graph – The graph.



read_only – (Optional) True to open in read-only mode. A read-only GraphDB cannot be written to.



返回

A GraphDB.



void Close()

Closes this Galaxy, turning it into an invalid state.



Private Functions



explicit Galaxy(lgraph::Galaxy *db)

inline Galaxy(const Galaxy&)

inline Galaxy &operator=(const Galaxy&)

Private Members



std::string user_

lgraph::Galaxy *db_

lgraph_result

Result interface for plugins and built-in procedures. The result of a plugin should be provided in this format in order for the Cypher engine and the graph visualizer to understand.



namespace lgraph

namespace cypher

namespace lgraph_api

Typedefs



typedef std::unordered_map<size_t, std::shared_ptr<lgraph_result::Node>> NODEMAP

typedef std::unordered_map<EdgeUid, std::shared_ptr<lgraph_result::Relationship>, EdgeUid::Hash> RELPMAP

class Record

#include <lgraph_result.h>

You only initialize the class by Result instance. Record provide some insert method to insert data to the record. eg. Insert, InsertVertexByID, InsertEdgeByID.



Public Functions



Record(const Record&)

Record(Record&&)

Record &operator=(const Record&)

Record &operator=(Record&&)

void Insert(const std::string &fname, const FieldData &fv)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – Field name you defined earlier.



fv – Field value.



void Insert(const std::string &fname, const int64_t vid, lgraph_api::Transaction *txn)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier. You can get properties and label from the interface, this is different from InsertVertexByID.



参数

fname – title name you defined earlier.



vid – VertextId



txn – Transaction



void Insert(const std::string &fname, EdgeUid &euid, lgraph_api::Transaction *txn)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier. You can get properties and label from the interface, this is different from InsertEdgeByID.



参数

fname – title name you defined earlier.



euid – EdgeUid



txn – Transaction



void InsertVertexByID(const std::string &fname, int64_t vid)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – Field name you defined earlier.



vid – VertextId.



void InsertEdgeByID(const std::string &fname, const EdgeUid &uid)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – title name you defined earlier.



uid – EdgeUid.



void Insert(const std::string &fname, const lgraph_api::VertexIterator &vit)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



vit – VertexIterator.



void Insert(const std::string &fname, const lgraph_api::InEdgeIterator &ieit)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



ieit – InEdgeIterator.



void Insert(const std::string &fname, const lgraph_api::OutEdgeIterator &oeit)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



oeit – OutEdgeIterator.



void Insert(const std::string &fname, const std::vector<FieldData> &list)

Insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



list – LIST OF FieldData.



void Insert(const std::string &fname, const std::map<std::string, FieldData> &map)

insert a value to result table. You can insert a value by insert function, and value type must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



map – MAP OF <string, FieldData>



void Insert(const std::string &fname, const traversal::Path &path, lgraph_api::Transaction *txn, NODEMAP &node_map, RELPMAP &relp_map)

insert value into result table. You can insert a value by the function, and value must be same as you defined earlier.



参数

fname – one of title name you defined earlier.



path – Path of traverse api.



txn – Trasaction



inline int64_t Size() const

Get the size of record. If record is empty, return 0, max size is not beyond the length of your defined param list



返回

Size of record.



inline bool HasKey(const std::string &key)

Check a key is exist or not. The key is the one of titile your defined earlier.



参数

key – The key.



返回

True if exsit, otherwise fasle.



Private Functions



explicit Record(const std::vector<std::pair<std::string, LGraphType>>&)

Private Members



std::unordered_map<std::string, std::shared_ptr<ResultElement>> record

std::unordered_map<std::string, LGraphType> header

int64_t length_

Friends



friend class Result

class Result

#include <lgraph_result.h>

Result table, result instance provide [MutableRecord], [ResetHeader], [Dump] and [Load] method. Table also provide some method to view content of table. For example, [Header] and [Recordview].



It’s worth noting that you are best to define your header before using result table. eg. auto result = Result({title, LGraphType}…) If you do not define header and initialize by Result(), you will get a empty table without header, you just use the table after using [ResetHeader] method to set your header.



Public Functions



Result()

Result(const std::initializer_list<std::pair<std::string, LGraphType>>&)

explicit Result(const std::vector<std::pair<std::string, LGraphType>>&)

LGraphType GetType(std::string title)

Get type of title.



参数

title – One of titles in table.



返回

LGraphType.



void ResetHeader(const std::vector<std::pair<std::string, LGraphType>> &header)

Reset your header, the operation will clear the original data and header, please use the function carefully.



参数

header – List of <title, LGraphType>



void ResetHeader(const std::initializer_list<std::pair<std::string, LGraphType>> &header)

Reset your header, the operation will clear the original data and header, please use the function carefully.



参数

header – List of <title, LGraphType>



Record *MutableRecord()

Create a new record in the table and return the record. The record is the reference of record in the table, if you want to modify the record, you must assign return value to a reference variable.



返回

The reference of record.



void Reserve(size_t n)

This function attempts to reserve enough memory for the result vector to hold the specified number of elements.



void Resize(size_t n)

This function will resize the vector to the specified number of elements



Record *At(size_t n)

Provides access to the data contained in the vector.



const std::vector<std::pair<std::string, LGraphType>> &Header()

return header of the table.



返回

header.



int64_t Size() const

return size of the table.



返回

table size.



std::string Dump(bool is_standard = true)

Serialize the table.



参数

is_standard – (Optional) If true, the result will serialize to a standard result, the standard result can be Visualized in web. If false, result will serialize a json object &#8212; SDK result.



返回

Serialize result.



void Load(const std::string &json)

Deserialize data to result table. This will be clear original data and header, please use this function carefully.



参数

json – Json string to be deserialized.



void ClearRecords()

Clear all the records, Size() will be 0.



std::vector<std::string> BoltHeader()

std::vector<std::vector<std::any>> BoltRecords()

inline void MarkPythonDriver(bool is_python_driver)

Mark that the result is returned to python driver. Python driver is special, use the virtual edge id instead of the real edge id



Private Functions



const std::unordered_map<std::string, std::shared_ptr<ResultElement>> &RecordView(int64_t row_num)

Get record of the table, if row number is more bigger than max length of table, throw a exception.



参数

row_num – row number of the table.



返回

One Record.



Private Members



std::vector<Record> result

std::vector<std::pair<std::string, LGraphType>> header

int64_t row_count_

bool is_python_driver_ = false

int64_t v_eid_ = 0

Friends



friend class lgraph::StateMachine

friend class cypher::PluginAdapter

namespace lgraph_result

lgraph_rpc_client

namespace fma_common

namespace lgraph_rpc

namespace lgraph

Enums



enum class GraphQueryType

Values:



enumerator CYPHER

enumerator GQL

enum ClientType

Values:



enumerator DIRECT_HA_CONNECTION

enumerator INDIRECT_HA_CONNECTION

enumerator SINGLE_CONNECTION

class RpcClient

#include <lgraph_rpc_client.h>

Public Functions



explicit RpcClient(const std::string &url, const std::string &user, const std::string &password)

RpcClient Login.



参数

url – Login address.



user – The username.



password – The password.



explicit RpcClient(std::vector<std::string> &urls, std::string user, std::string password)

RpcClient Login.



参数

urls – Login address.



user – The username.



password – The password.



~RpcClient()

bool CallCypher(std::string &result, const std::string &cypher, const std::string &graph = "default", bool json_format = true, double timeout = 0, const std::string &url = "")

Execute a cypher query



参数

result – [out] The result.



cypher – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



url – [in] (Optional) Node address of calling cypher.



返回

True if it succeeds, false if it fails.



bool CallCypherToLeader(std::string &result, const std::string &cypher, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Execute a cypher query to leader



参数

result – [out] The result.



cypher – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool CallGql(std::string &result, const std::string &gql, const std::string &graph = "default", bool json_format = true, double timeout = 0, const std::string &url = "")

Execute a gql query



参数

result – [out] The result.



gql – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



url – [in] (Optional) Node address of calling cypher.



返回

True if it succeeds, false if it fails.



bool CallGqlToLeader(std::string &result, const std::string &gql, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Execute a gql query to leader



参数

result – [out] The result.



gql – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool CallProcedure(std::string &result, const std::string &procedure_type, const std::string &procedure_name, const std::string &param, double procedure_time_out = 0.0, bool in_process = false, const std::string &graph = "default", bool json_format = true, const std::string &url = "")

Execute a user-defined procedure



参数

result – [out] The result.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



param – [in] the execution parameters.



procedure_time_out – [in] (Optional) Maximum execution time, overruns will be interrupted.



in_process – [in] (Optional) support in future.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



url – [in] (Optional) Node address of calling procedure.



返回

True if it succeeds, false if it fails.



bool CallProcedureToLeader(std::string &result, const std::string &procedure_type, const std::string &procedure_name, const std::string &param, double procedure_time_out = 0.0, bool in_process = false, const std::string &graph = "default", bool json_format = true)

Execute a user-defined procedure to leader



参数

result – [out] The result.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



param – [in] the execution parameters.



procedure_time_out – [in] (Optional) Maximum execution time, overruns will be interrupted.



in_process – [in] (Optional) support in future.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



返回

True if it succeeds, false if it fails.



bool LoadProcedure(std::string &result, const std::string &source_file, const std::string &procedure_type, const std::string &procedure_name, const std::string &code_type, const std::string &procedure_description, bool read_only, const std::string &version = "v1", const std::string &graph = "default")

Load a built-in procedure



参数

result – [out] The result.



source_file – [in] the source_file contain procedure code.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



code_type – [in] code type, currently supported PY, SO, CPP, ZIP.



procedure_description – [in] procedure description.



read_only – [in] procedure is read only or not.



version – [in] (Optional) the version of procedure.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool LoadProcedure(std::string &result, const std::vector<std::string> &source_files, const std::string &procedure_type, const std::string &procedure_name, const std::string &code_type, const std::string &procedure_description, bool read_only, const std::string &version = "v1", const std::string &graph = "default")

Load a built-in procedure



参数

result – [out] The result.



source_files – [in] the source_file list contain procedure code(only for code_type cpp)



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



code_type – [in] code type, currently supported PY, SO, CPP, ZIP.



procedure_description – [in] procedure description.



read_only – [in] procedure is read only or not.



version – [in] (Optional) the version of procedure.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool ListProcedures(std::string &result, const std::string &procedure_type, const std::string &version = "any", const std::string &graph = "default", const std::string &url = "")

List user-defined procedures



参数

result – [out] The result.



procedure_type – [in] (Optional) the procedure type, “” for all procedures, CPP and PY for special type.



version – [in] (Optional) the version of procedure.



graph – [in] (Optional) the graph to query.



url – [in] Node address of calling procedure.



返回

True if it succeeds, false if it fails.



bool DeleteProcedure(std::string &result, const std::string &procedure_type, const std::string &procedure_name, const std::string &graph = "default")

Execute a user-defined procedure



参数

result – [out] The result.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool ImportSchemaFromContent(std::string &result, const std::string &schema, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge schema from content string



参数

result – [out] The result.



schema – [in] the schema to be imported.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportDataFromContent(std::string &result, const std::string &desc, const std::string &data, const std::string &delimiter, bool continue_on_error = false, int thread_nums = 8, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge data from content string



参数

result – [out] The result.



desc – [in] data format description.



data – [in] the data to be imported.



delimiter – [in] data separator.



continue_on_error – [in] (Optional) whether to continue when importing data fails.



thread_nums – [in] (Optional) maximum number of threads.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportSchemaFromFile(std::string &result, const std::string &schema_file, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge schema from file



参数

result – [out] The result.



schema_file – [in] the schema_file contain schema.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportDataFromFile(std::string &result, const std::string &conf_file, const std::string &delimiter, bool continue_on_error = false, int thread_nums = 8, int skip_packages = 0, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge data from file



参数

result – [out] The result.



conf_file – [in] data file contain format description and data.



delimiter – [in] data separator.



continue_on_error – [in] (Optional) whether to continue when importing data fails.



thread_nums – [in] (Optional) maximum number of threads.



skip_packages – [in] (Optional) skip packages number.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



int64_t Restore(const std::vector<BackupLogEntry> &requests)

void Logout()

Client log out



Private Functions



bool IsReadQuery(lgraph::GraphQueryType type, const std::string &query, const std::string &graph)

Determine whether it is a read-only query



参数

type – [in] inquire query type.



query – [in] inquire statement.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



std::shared_ptr<lgraph::RpcClient::RpcSingleClient> GetClient(lgraph::GraphQueryType type, const std::string &cypher, const std::string &graph)

Return rpc client based on whether it is a read-only query



参数

type – [in] inquire query type.



query – [in] inquire statement.



graph – [in] (Optional) the graph to query.



返回

Master rpc client if cypher is not read-only, slaver rpc client if cypher is read-only.



std::shared_ptr<lgraph::RpcClient::RpcSingleClient> GetClient(bool isReadQuery)

Return rpc client based on whether it is a read-only query



参数

isReadQuery – [in] read query or not.



返回

Master rpc client if cypher is not read-only, slaver rpc client if cypher is read-only.



std::shared_ptr<lgraph::RpcClient::RpcSingleClient> GetClientByNode(const std::string &url)

Get the client according to the node url



参数

url – [in] Node address of client connection.



返回

Rpc client connecting to url.



void RefreshUserDefinedProcedure()

Refresh User-defined Procedure



void RefreshBuiltInProcedure()

Refresh Built-in Procedure



void RefreshClientPool()

Refresh the client connection pool according to the cluster status



void LoadBalanceClientPool()

Load balance the client pool



void RefreshConnection()

Refresh client pool, procedure info



template<typename F>

bool DoubleCheckQuery(F const &f)

If an exception is thrown in the query, refresh the connection and re-execute



Private Members



ClientType client_type

std::string user

std::string password

std::shared_ptr<lgraph::RpcClient::RpcSingleClient> base_client

std::vector<std::string> urls

std::shared_ptr<lgraph::RpcClient::RpcSingleClient> leader_client

std::deque<std::shared_ptr<lgraph::RpcClient::RpcSingleClient>> client_pool

nlohmann::json built_in_procedures = {}

nlohmann::json user_defined_procedures = {}

std::vector<std::string> cypher_write_constant

std::vector<std::string> gql_write_constant

class RpcSingleClient

Public Functions



RpcSingleClient(const std::string &url, const std::string &user, const std::string &password)

RpcSingleClient Login.



参数

url – Login address.



user – The username.



password – The password.



~RpcSingleClient()

int64_t Restore(const std::vector<BackupLogEntry> &requests)

bool LoadProcedure(std::string &result, const std::vector<std::string> &source_files, const std::string &procedure_type, const std::string &procedure_name, const std::string &code_type, const std::string &procedure_description, bool read_only, const std::string &version = "v1", const std::string &graph = "default")

Load a user-defined procedure



参数

result – [out] The result.



source_files – [in] the source_file list contain procedure code(only for code_type cpp)



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



code_type – [in] code type, currently supported PY, SO, CPP, ZIP.



procedure_description – [in] procedure description.



read_only – [in] procedure is read only or not.



version – [in] (Optional) the version of procedure.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool CallProcedure(std::string &result, const std::string &procedure_type, const std::string &procedure_name, const std::string &param, double procedure_time_out = 0.0, bool in_process = false, const std::string &graph = "default", bool json_format = true)

Execute a user-defined procedure



参数

result – [out] The result.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



param – [in] the execution parameters.



procedure_time_out – [in] (Optional) Maximum execution time, overruns will be interrupted.



in_process – [in] (Optional) support in future.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json， Otherwise, binary format.



返回

True if it succeeds, false if it fails.



bool ListProcedures(std::string &result, const std::string &procedure_type, const std::string &version = "any", const std::string &graph = "default")

List user-defined procedures



参数

result – [out] The result.



procedure_type – [in] (Optional) the procedure type, “” for all procedures, CPP and PY for special type.



version – [in] (Optional) the version of procedure.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool DeleteProcedure(std::string &result, const std::string &procedure_type, const std::string &procedure_name, const std::string &graph = "default")

Execute a user-defined procedure



参数

result – [out] The result.



procedure_type – [in] the procedure type, currently supported CPP and PY.



procedure_name – [in] procedure name.



graph – [in] (Optional) the graph to query.



返回

True if it succeeds, false if it fails.



bool ImportSchemaFromFile(std::string &result, const std::string &schema_file, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge schema from file



参数

result – [out] The result.



schema_file – [in] the schema_file contain schema.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportDataFromFile(std::string &result, const std::string &conf_file, const std::string &delimiter, bool continue_on_error = false, int thread_nums = 8, int skip_packages = 0, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge data from file



参数

result – [out] The result.



conf_file – [in] data file contain format description and data.



delimiter – [in] data separator.



continue_on_error – [in] (Optional) whether to continue when importing data fails.



thread_nums – [in] (Optional) maximum number of threads.



skip_packages – [in] (Optional) skip packages number.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportSchemaFromContent(std::string &result, const std::string &schema, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge schema from content string



参数

result – [out] The result.



schema – [in] the schema to be imported.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool ImportDataFromContent(std::string &result, const std::string &desc, const std::string &data, const std::string &delimiter, bool continue_on_error = false, int thread_nums = 8, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Import vertex or edge data from content string



参数

result – [out] The result.



desc – [in] data format description.



data – [in] the data to be imported.



delimiter – [in] data separator.



continue_on_error – [in] (Optional) whether to continue when importing data fails.



thread_nums – [in] (Optional) maximum number of threads.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool CallCypher(std::string &result, const std::string &cypher, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Execute a cypher query



参数

result – [out] The result.



cypher – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



bool CallGql(std::string &result, const std::string &gql, const std::string &graph = "default", bool json_format = true, double timeout = 0)

Execute a gql query



参数

result – [out] The result.



gql – [in] inquire statement.



graph – [in] (Optional) the graph to query.



json_format – [in] (Optional) Returns the format， true is json，Otherwise, binary format.



timeout – [in] (Optional) Maximum execution time, overruns will be interrupted.



返回

True if it succeeds, false if it fails.



std::string GetUrl()

Get the url of single client.



返回

the url of single client.



void Logout()

Client log out



Private Functions



LGraphResponse HandleRequest(LGraphRequest *req)

bool HandleGraphQueryRequest(lgraph::GraphQueryType type, LGraphResponse *res, const std::string &query, const std::string &graph, bool json_format, double timeout)

std::string GraphQueryResponseExtractor(const GraphQueryResponse &cypher)

Private Members



std::string url

std::string user

std::string password

std::string token

int64_t server_version

std::shared_ptr<lgraph_rpc::m_channel> channel

std::shared_ptr<lgraph_rpc::m_controller> cntl

std::shared_ptr<lgraph_rpc::m_channel_options> options

lgraph_traversal

namespace lgraph_api

namespace traversal

Functions



ParallelVector<size_t> FindVertices(GraphDB &db, Transaction &txn, std::function<bool(VertexIterator&)> filter, bool parallel = false)

Retrieve all vertices passing the specified filter. Note that if the transaction is not read-only, parallel will be ignored (i.e. parallelism will not be available).



参数

db – [inout] The GraphDB instance.



txn – [inout] The transaction.



filter – [inout] The user-defined filter function.



parallel – (Optional) Enable parallelism or not.



返回

The corresponding list of vertices.



template<typename VertexData>

static ParallelVector<VertexData> ExtractVertexData(GraphDB &db, Transaction &txn, ParallelVector<size_t> &frontier, std::function<void(VertexIterator&, VertexData&)> extract, bool parallel = false)

Extract data from specified vertices. Note that if the transaction is not read-only, parallel will be ignored (i.e. parallelism will not be available).



抛出

std::runtime_error – Raised when a runtime error condition occurs.



模板参数

VertexData – Type of the vertex data.



参数

db – [inout] The database.



txn – [inout] The transaction.



frontier – [inout] The vertices to extract data from.



extract – [inout] The user-defined extract function.



parallel – (Optional) Enable parallelism or not.



返回

The corresponding extracted data.



template<class IT>

bool DefaultFilter(IT &it)

The default filter you may use.



模板参数

IT – Type of the iterator.



参数

it – [inout] An iterator class.



返回

Always true.



template<class IT>

std::function<bool(IT&)> LabelEquals(const std::string &label)

Function closure filtering by label.



模板参数

IT – Type of the iterator.



参数

label – An iterator class.



返回

The filter function.



template<class IT>

std::function<bool(IT&)> LabelEquals(size_t label_id)

Function closure filtering by label id.



模板参数

IT – Type of the iterator.



参数

label_id – An iterator class.



返回

The filter function.



bool operator==(const Vertex &lhs, const Vertex &rhs)

bool operator!=(const Vertex &lhs, const Vertex &rhs)

bool operator==(const Edge &lhs, const Edge &rhs)

bool operator!=(const Edge &lhs, const Edge &rhs)

Variables



static constexpr size_t MAX_RESULT_SIZE = 1ul << 36

static constexpr size_t TRAVERSAL_PARALLEL = 1ul << 0

static constexpr size_t TRAVERSAL_ALLOW_REVISITS = 1ul << 1

class Edge

#include <lgraph_traversal.h>

Represent an edge.



Public Functions



Edge(size_t start, uint16_t lid, uint64_t tid, size_t end, size_t eid, bool forward)

Constructor



参数

start – The start.



lid – The lid.



tid – The tid.



end – The end.



eid – The eid.



forward – True to forward.



Edge(const Edge &rhs) = default

Copy constructor



参数

rhs – The right hand side.



Vertex GetStartVertex() const

Get the start vertex of this edge.



返回

The start vertex.



Vertex GetEndVertex() const

Get the end vertex of this edge.



返回

The end vertex.



uint16_t GetLabelId() const

Get the label ID.



返回

The label ID.



uint64_t GetTemporalId() const

Get the Temporal ID.



返回

The temporal ID.



size_t GetEdgeId() const

Get the edge ID.



返回

The edge ID.



bool IsForward() const

Get the direction of this edge.



返回

true : forward; false: backward.



Vertex GetSrcVertex() const

Get the source vertex of this edge.



返回

The source vertex.



Vertex GetDstVertex() const

Get the destination vertex of this edge.



返回

The destination vertex.



Private Members



size_t start_

size_t end_

size_t eid_

uint16_t lid_

int64_t tid_

bool forward_

Friends



friend class Path

friend class IteratorHelper

friend class PathTraversal

class FrontierTraversal

#include <lgraph_traversal.h>

FrontierTraversal provides the most common way to traverse graphs. You can start from a single vertex or a set of vertices (known as the initial frontier), and expand them frontier by frontier, each time visiting neighboring vertices of the current frontier and make those matching specified conditions the new frontier. One powerful feature of FrontierTraversal is that the traversal can be performed in parallel, accelerating those deep queries significantly.



Public Functions



FrontierTraversal(GraphDB &db, Transaction &txn, size_t flags = 0, size_t capacity = MAX_RESULT_SIZE)

Construct the FrontierTraversal object. Note that the transaction must be read- only if you want to perform the traversals in parallel (i.e. TRAVERSAL_PARALLEL is specified in flags). Be careful when TRAVERSAL_ALLOW_REVISITS is used, as each vertex may be visited more than once, making the result set huge.



参数

db – [inout] The GraphDB instance.



txn – [inout] The transaction.



flags – (Optional) The options used during traversals.



ParallelVector<size_t> &GetFrontier()

Retrieve the current (i.e. latest) frontier.



返回

The frontier.



void SetFrontier(size_t root_vid)

Set the (initial) frontier to contain a single vertex.



参数

root_vid – The identifer for the starting vertex.



void SetFrontier(ParallelVector<size_t> &root_vids)

Set the (initial) frontier to contain a set of vertices.



参数

root_vids – [inout] The starting vertex identifiers.



void SetFrontier(std::function<bool(VertexIterator&)> root_vertex_filter)

Set the (initial) frontier by using a filter function. Each vertex will be checked against the specified filter.



参数

root_vertex_filter – [inout] The filter function.



void ExpandOutEdges(std::function<bool(OutEdgeIterator&)> out_edge_filter = nullptr, std::function<bool(VertexIterator&)> out_neighbour_filter = nullptr)

Expand the current frontier through outgoing edges using filters. Note that the default value for the two filters (nullptr) means all the expansions of this level should succeed and enables some optimizations.



参数

out_edge_filter – [inout] (Optional) The filter for an outgoing edge.



out_neighbour_filter – [inout] (Optional) The filter for an destination vertex.



void ExpandInEdges(std::function<bool(InEdgeIterator&)> in_edge_filter = nullptr, std::function<bool(VertexIterator&)> in_neighbour_filter = nullptr)

Expand the current frontier through incoming edges using filters. Note that the default value for the two filters (nullptr) means all the expansions of this level should succeed and enables some optimizations.



参数

in_edge_filter – [inout] (Optional) The filter for an incoming edge.



in_neighbour_filter – [inout] (Optional) The filter for an source vertex.



void ExpandEdges(std::function<bool(OutEdgeIterator&)> out_edge_filter = nullptr, std::function<bool(InEdgeIterator&)> in_edge_filter = nullptr, std::function<bool(VertexIterator&)> out_neighbour_filter = nullptr, std::function<bool(VertexIterator&)> in_neighbour_filter = nullptr)

Expand the current frontier through both directions using filters. Note that the default value for the two filters (nullptr) means all the expansions of this level should succeed and enables some optimizations.



参数

out_edge_filter – [inout] (Optional) The filter for an outgoing edge.



in_edge_filter – [inout] (Optional) The filter for an incoming edge.



out_neighbour_filter – [inout] (Optional) The filter for an destination vertex.



in_neighbour_filter – [inout] (Optional) The filter for an source vertex.



void Reset()

Reset the traversal.



void ResetVisited()

Reset only the visited flags.



Private Members



GraphDB &db_

Transaction &txn_

size_t flags_

size_t num_vertices_

ParallelVector<size_t> curr_frontier_

ParallelVector<size_t> next_frontier_

ParallelBitset visited_

class IteratorHelper

#include <lgraph_traversal.h>

IteratorHelper provides some useful methods, such as casting Vertex/Edge objects to their iterator forms.



Public Functions



explicit IteratorHelper(Transaction &txn)

Constructor



参数

txn – [inout] The transaction.



VertexIterator Cast(const Vertex &vertex)

Casting a Vertex to a VertexIterator.



参数

vertex – A Vertex object.



返回

A VertexIterator corresponding to vertex.



OutEdgeIterator Cast(const Edge &edge)

Casting an Edge to an OutEdgeIterator.



参数

edge – An edge object.



返回

An OutEdgeIterator corresponding to edge.



Private Members



Transaction &txn_

class Path

#include <lgraph_traversal.h>

Represent a path.



Public Functions



explicit Path(const Vertex &start)

Constructor



参数

start – The start.



Path(const Path &rhs)

Copy constructor



参数

rhs – The right hand side.



Path(Path &&rhs) = delete

Move constructor



参数

rhs – [inout] The right hand side.



Path &operator=(const Path &rhs)

Assignment operator



参数

rhs – The right hand side.



返回

A shallow copy of this object.



Path &operator=(Path &&rhs) = delete

Move assignment operator



参数

rhs – [inout] The right hand side.



返回

A shallow copy of this object.



size_t Length() const

Get the length of this path.



返回

The path length.



void Append(const Edge &edge)

Append an edge to the path. Note that the edge’s start vertex should match the current path’s end vertex.



参数

edge – edge to append.



Vertex GetStartVertex() const

Get the start vertex of this path.



Vertex GetEndVertex() const

Get the end vertex of this path.



Edge GetLastEdge() const

Get the last edge of this path.



Edge GetNthEdge(size_t n) const

Get the Nth edge of this path. The available range of N is [0, Length).



Vertex GetNthVertex(size_t n) const

Get the Nth vertex of this path. The available range of N is [0, Length].



Private Members



std::vector<bool> dirs_

std::vector<uint16_t> lids_

std::vector<size_t> ids_

class PathTraversal

#include <lgraph_traversal.h>

PathTraversal behaves similar to FrontierTraversal, except that 1) Each vertex could be revisited multiple times. 2) Each traversed path would be stored, and the filter function has access to the path.



Public Functions



PathTraversal(GraphDB &db, Transaction &txn, size_t flags, size_t capacity = MAX_RESULT_SIZE)

Construct the PathTraversal object. Note that the transaction must be read-only if you want to perform the traversals in parallel (i.e. TRAVERSAL_PARALLEL is specified in flags). Since TRAVERSAL_ALLOW_REVISITS is implied in PathTraversal and storing the Paths also takes a lot of space, the memory consumption could be very large if the filters are not very selective.



参数

db – [inout] The GraphDB instance.



txn – [inout] The transaction.



flags – The options used during traversals.



ParallelVector<Path> &GetFrontier()

Retrieve the current (i.e. latest) frontier.



返回

The frontier.



void SetFrontier(size_t root_vid)

Set the (initial) frontier to contain a single vertex.



参数

root_vid – The identifer for the starting vertex.



void SetFrontier(ParallelVector<size_t> &root_vids)

Set the (initial) frontier to contain a set of vertices.



参数

root_vids – [inout] The starting vertex identifiers.



void SetFrontier(std::function<bool(VertexIterator&)> root_vertex_filter)

Set the (initial) frontier by using a filter function. Each vertex will be checked against the specified filter.



参数

root_vertex_filter – [inout] The filter function.



void ExpandOutEdges(std::function<bool(OutEdgeIterator&, Path&, IteratorHelper&)> out_edge_filter = nullptr, std::function<bool(VertexIterator&, Path&, IteratorHelper&)> out_neighbour_filter = nullptr)

Expand the current frontier through outgoing edges using filters.



参数

out_edge_filter – [inout] (Optional) The filter for an outgoing edge.



out_neighbour_filter – [inout] (Optional) The filter for an destination vertex.



void ExpandInEdges(std::function<bool(InEdgeIterator&, Path&, IteratorHelper&)> in_edge_filter = nullptr, std::function<bool(VertexIterator&, Path&, IteratorHelper&)> in_neighbour_filter = nullptr)

Expand the current frontier through incoming edges using filters.



参数

in_edge_filter – [inout] (Optional) The filter for an incoming edge.



in_neighbour_filter – [inout] (Optional) The filter for an source vertex.



void ExpandEdges(std::function<bool(OutEdgeIterator&, Path&, IteratorHelper&)> out_edge_filter = nullptr, std::function<bool(InEdgeIterator&, Path&, IteratorHelper&)> in_edge_filter = nullptr, std::function<bool(VertexIterator&, Path&, IteratorHelper&)> out_neighbour_filter = nullptr, std::function<bool(VertexIterator&, Path&, IteratorHelper&)> in_neighbour_filter = nullptr)

Expand the current frontier through both directions using filters.



参数

out_edge_filter – [inout] (Optional) The filter for an outgoing edge.



in_edge_filter – [inout] (Optional) The filter for an incoming edge.



out_neighbour_filter – [inout] (Optional) The filter for an destination vertex.



in_neighbour_filter – [inout] (Optional) The filter for an source vertex.



void Reset()

Reset the traversal.



Private Members



GraphDB &db_

Transaction &txn_

size_t flags_

size_t num_vertices_

ParallelVector<Path> curr_frontier_

ParallelVector<Path> next_frontier_

class Vertex

#include <lgraph_traversal.h>

Represent a vertex.



Public Functions



explicit Vertex(size_t vid)

Constructor



参数

vid – The vid.



Vertex(const Vertex &rhs) = default

Copy constructor



参数

rhs – The right hand side.



size_t GetId() const

Get the Id of this vertex.



返回

The Id.



Private Members



size_t vid_

Friends



friend class Path

friend class IteratorHelper

friend class PathTraversal

lgraph_txn

namespace lgraph

namespace lgraph_api

class Transaction

#include <lgraph_txn.h>

TuGraph operations happen in transactions. A transaction is sequence of operations that is carried out atomically on the GraphDB. TuGraph transactions provides full ACID guarantees.



Transactions are created using GraphDB::CreateReadTxn() and GraphDB::CreateWriteTxn(). A read transaction can only perform read operations, otherwise an exception is thrown. A write transaction can perform reads as well as writes. There are performance differences between read and write operations. So if you only need read in a transaction, you should create a read transaction.



Each transaction must be used in one thread only, and they should not be passed from one thread to another unless it is a forked transaction.



Read transactions can be forked. The new copy of the transaction will have the same view as the forked one, and it can be used in a separate thread. By forking from one read transaction and using the forked copies in different threads, we can parallelize the execution of specific operations. For example, you can implement a parallel BFS with this capability. Also, you can dump a snapshot of the whole graph using



Public Functions



Transaction(Transaction &&rhs) = default

Transaction &operator=(Transaction &&rhs) = default

Transaction(const Transaction&) = delete

Transaction &operator=(const Transaction&) = delete

void Commit()

Commits this transaction. Note that optimistic write transactions may fail to commit (an TxnConflict would be thrown).



void Abort()

Aborts this transaction.



bool IsValid() const

Query if this transaction is valid. Transaction becomes invalid after calling Abort() or Commit(). Operations on invalid transaction yields exceptions.



返回

True if valid, false if not.



bool IsReadOnly() const

Query if this txn is read only



返回

True if read only, false if not.



const std::shared_ptr<lgraph::Transaction> GetTxn()

Get Transaction



返回

Transaction



VertexIterator GetVertexIterator()

Get a vertex iterator pointing to the first vertex. If there is no vertex, the iterator is invalid.



返回

The vertex iterator.



VertexIterator GetVertexIterator(int64_t vid, bool nearest = false)

Gets a vertex iterator pointing to the Vertex with vid. If the vertex does not exist, the iterator is invalid. If nearest==true, the iterator points to the first vertex sorted by vid, with id>=vid.



参数

vid – The vid.



nearest – (Optional) True to point to the nearest vertex sorted by vid.



返回

The vertex iterator.



OutEdgeIterator GetOutEdgeIterator(const EdgeUid &euid, bool nearest = false)

Gets an out edge iterator pointing to the edge specified by euid. If nearest==true, and the specified edge does not exist, return the first edge that sorts after the specified one.



参数

euid – Edge Unique Id.



nearest – (Optional) If true, get the first edge that sorts after the specified one if the specified one does not exist.



返回

The out edge iterator.



OutEdgeIterator GetOutEdgeIterator(const int64_t src, const int64_t dst, const int16_t lid)

InEdgeIterator GetInEdgeIterator(const EdgeUid &euid, bool nearest = false)

Gets an in edge iterator pointing to the edge specified by euid. If nearest==true, and the specified edge does not exist, return the first edge that sorts after the specified one.



参数

euid – Edge Unique Id.



nearest – (Optional) If true, get the first edge that sorts after the specified one if the specified one does not exist.



返回

The out edge iterator.



InEdgeIterator GetInEdgeIterator(const int64_t src, const int64_t dst, const int16_t lid)

size_t GetNumVertexLabels()

Gets number of vertex labels



返回

The number of vertex labels.



size_t GetNumEdgeLabels()

Gets number of edge labels.



返回

The number of edge labels.



std::vector<std::string> ListVertexLabels()

Lists all vertex labels.



返回

Label names.



std::vector<std::string> ListEdgeLabels()

List all edge labels



返回

Label names.



size_t GetVertexLabelId(const std::string &label)

Gets vertex label id corresponding to the label name.



参数

label – The label name.



返回

The label id.



size_t GetEdgeLabelId(const std::string &label)

Gets edge label id corresponding to the label name.



参数

label – The label.



返回

The edge label id.



std::vector<FieldSpec> GetVertexSchema(const std::string &label)

Gets edge schema definition corresponding to the vertex label.



参数

label – The label.



返回

The schema.



std::vector<FieldSpec> GetEdgeSchema(const std::string &label)

Gets edge schema definition corresponding to the edge label.



参数

label – The label.



返回

The edge schema.



size_t GetVertexFieldId(size_t label_id, const std::string &field_name)

Gets vertex field id.



参数

label_id – Identifier for the label.



field_name – Field name.



返回

The vertex field identifiers.



std::vector<size_t> GetVertexFieldIds(size_t label_id, const std::vector<std::string> &field_names)

Gets vertex field ids.



参数

label_id – Identifier for the label.



field_names – Field names.



返回

The vertex field identifiers.



size_t GetEdgeFieldId(size_t label_id, const std::string &field_name)

Gets edge field id.



参数

label_id – Identifier for the label.



field_name – Field name.



返回

The edge field identifier.



std::vector<size_t> GetEdgeFieldIds(size_t label_id, const std::vector<std::string> &field_names)

Gets edge field ids.



参数

label_id – Identifier for the label.



field_names – Field names.



返回

The edge field identifier.



int64_t AddVertex(const std::string &label_name, const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Adds a vertex. All non-nullable fields must be specified. VertexIndex is also updated. If a unique_id is indexed for the vertex, and the same unique_id exists, an exception is thrown.



参数

label_name – Name of the label.



field_names – List of names of the fields.



field_value_strings – The field values in string representation.



返回

Vertex id of the new vertex.



int64_t AddVertex(const std::string &label_name, const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Adds a vertex. All non-nullable fields must be specified. VertexIndex is also updated. If a unique_id is indexed for the vertex, and the same unique_id exists, an exception is thrown.



参数

label_name – Name of the label.



field_names – List of names of the fields.



field_values – The field values.



返回

Vertex id of the new vertex.



int64_t AddVertex(size_t label_id, const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Adds a vertex. All non-nullable fields must be specified. VertexIndex is also updated. If a unique_id is indexed for the vertex, and the same unique_id exists, an exception is thrown.



参数

label_id – Label id.



field_ids – List of field ids.



field_values – The field values.



返回

Vertex id of the new vertex.



int UpsertVertex(size_t label_id, size_t primary_pos, const std::vector<size_t> &unique_pos, const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Upsert a vertex.



参数

label_id – Label id.



primary_pos – The location of the primary field in field_ids.



unique_pos – The locations of the unique index field in field_ids, can be empty.



field_ids – List of field ids.



field_values – The field values.



返回

0: nothing happened because of index conflict 1: the vertex is inserted 2: the vertex is updated



EdgeUid AddEdge(int64_t src, int64_t dst, const std::string &label, const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Adds an edge. All non-nullable fields must be specified. An exception is thrown if src or dst does not exist.



参数

src – Source vertex id.



dst – Destination vertex id.



label – The label name.



field_names – List of field names.



field_value_strings – List of field values in string representation.



返回

EdgeUid of the new edge.



EdgeUid AddEdge(int64_t src, int64_t dst, const std::string &label, const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Adds an edge. All non-nullable fields must be specified. An exception is thrown if src or dst does not exist.



参数

src – Source vertex id.



dst – Destination vertex id.



label – The label name.



field_names – List of field names.



field_values – List of field values.



返回

EdgeUid of the new edge.



EdgeUid AddEdge(int64_t src, int64_t dst, size_t label_id, const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Adds an edge. All non-nullable fields must be specified. An exception is thrown if src or dst does not exist.



参数

src – Source vertex id.



dst – Destination vertex id.



label_id – The label id.



field_ids – List of field ids.



field_values – List of field values.



返回

EdgeUid of the new edge.



bool UpsertEdge(int64_t src, int64_t dst, const std::string &label, const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Upsert edge. If there is no src->dst edge, insert it. Otherwise, try to update the edge’s property. If the edge exists and the label differs from specified label, an exception is thrown.



参数

src – Source vertex id.



dst – Destination vertex id.



label – The label name.



field_names – List of field names.



field_value_strings – List of field values in string representation.



返回

True if the edge is inserted, false if the edge is updated.



bool UpsertEdge(int64_t src, int64_t dst, const std::string &label, const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Upsert edge. If there is no src->dst edge, insert it. Otherwise, try to update the edge’s property. If the edge exists and the label differs from specified label, an exception is thrown.



参数

src – Source vertex id.



dst – Destination vertex id.



label – The label name.



field_names – List of field names.



field_values – List of field values.



返回

True if the edge is inserted, false if the edge is updated.



bool UpsertEdge(int64_t src, int64_t dst, size_t label_id, const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Upsert edge. If there is no src->dst edge, insert it. Otherwise, try to update the edge’s property. If the edge exists and the label differs from specified label, an exception is thrown.



参数

src – Source vertex id.



dst – Destination vertex id.



label_id – The label id.



field_ids – List of field ids.



field_values – List of field values.



返回

True if the edge is inserted, false if the edge is updated.



int UpsertEdge(int64_t src, int64_t dst, size_t label_id, const std::vector<size_t> &unique_pos, const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values, std::optional<size_t> pair_unique_pos)

Upsert edge. If there is no src->dst edge, insert it. Otherwise, try to update the edge’s property.



参数

src – Source vertex id.



dst – Destination vertex id.



label_id – The label id.



unique_pos – The locations of the unique index field in field_ids, can be empty.



field_ids – List of field ids.



field_values – List of field values.



返回

0: nothing happened because of index conflict 1: the vertex is inserted 2: the vertex is updated



std::vector<IndexSpec> ListVertexIndexes()

List indexes



返回

A vector of vertex index specs.



std::vector<CompositeIndexSpec> ListVertexCompositeIndexes()

List indexes



返回

A vector of vertex composite index specs.



std::vector<IndexSpec> ListEdgeIndexes()

List indexes



返回

A vector of edge index specs.



VertexIndexIterator GetVertexIndexIterator(size_t label_id, size_t field_id, const FieldData &key_start, const FieldData &key_end)

Gets vertex index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all vertexes that has field value v.



参数

label_id – The label id.



field_id – The field id.



key_start – The key start.



key_end – The key end, inclusive.



返回

The index iterator.



VertexCompositeIndexIterator GetVertexCompositeIndexIterator(size_t label_id, const std::vector<size_t> &field_id, const std::vector<FieldData> &key_start, const std::vector<FieldData> &key_end)

EdgeIndexIterator GetEdgeIndexIterator(size_t label_id, size_t field_id, const FieldData &key_start, const FieldData &key_end)

Gets edge index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all edges that has field value v.



参数

label_id – The label id.



field_id – The field id.



key_start – The key start.



key_end – The key end, inclusive.



返回

The index iterator.



EdgeIndexIterator GetEdgePairUniqueIndexIterator(size_t label_id, size_t field_id, int64_t src_vid, int64_t dst_vid, const FieldData &key_start, const FieldData &key_end)

VertexIndexIterator GetVertexIndexIterator(const std::string &label, const std::string &field, const FieldData &key_start, const FieldData &key_end)

Gets vertex index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all vertexes that has field value v.



参数

label – The label.



field – The field.



key_start – The key start.



key_end – The key end, inclusive.



返回

The index iterator.



VertexCompositeIndexIterator GetVertexCompositeIndexIterator(const std::string &label, const std::vector<std::string> &field, const std::vector<FieldData> &key_start, const std::vector<FieldData> &key_end)

EdgeIndexIterator GetEdgeIndexIterator(const std::string &label, const std::string &field, const FieldData &key_start, const FieldData &key_end)

Gets index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all edges that has field value v.



参数

label – The label.



field – The field.



key_start – The key start.



key_end – The key end, inclusive.



返回

The index iterator.



VertexIndexIterator GetVertexIndexIterator(const std::string &label, const std::string &field, const std::string &key_start, const std::string &key_end)

Gets index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all vertexes that has field value v.



参数

label – The label.



field – The field.



key_start – The key start.



key_end – The key end.



返回

The index iterator.



VertexCompositeIndexIterator GetVertexCompositeIndexIterator(const std::string &label, const std::vector<std::string> &field, const std::vector<std::string> &key_start, const std::vector<std::string> &key_end)

EdgeIndexIterator GetEdgeIndexIterator(const std::string &label, const std::string &field, const std::string &key_start, const std::string &key_end)

Gets index iterator. The iterator has field value [key_start, key_end]. So key_start=key_end=v returns an iterator pointing to all edges that has field value v.



参数

label – The label.



field – The field.



key_start – The key start.



key_end – The key end.



返回

The index iterator.



bool IsVertexIndexed(const std::string &label, const std::string &field)

Query if index is ready for use. This should be used only to decide whether to use an index. To wait for an index to be ready, use lgraphDB::WaitIndexReady().



VertexIndex building is async, especially when added for a (label, field) that already has a lot of vertices. This function tells us if the index building is finished.



DO NOT wait for index building in a transaction. Write transactions block other write transactions, so blocking in a write transaction is always a bad idea. And long-living read transactions interfere with GC, making the DB grow unexpectly.



参数

label – The label.



field – The field.



返回

True if index ready, false if not.



bool IsEdgeIndexed(const std::string &label, const std::string &field)

Query if index is ready for use. This should be used only to decide whether to use an index. To wait for an index to be ready, use lgraphDB::WaitIndexReady().



VertexIndex building is async, especially when added for a (label, field) that already has a lot of edges. This function tells us if the index building is finished.



DO NOT wait for index building in a transaction. Write transactions block other write transactions, so blocking in a write transaction is always a bad idea. And long-living read transactions interfere with GC, making the DB grow unexpectly.



参数

label – The label.



field – The field.



返回

True if index ready, false if not.



VertexIterator GetVertexByUniqueIndex(const std::string &label_name, const std::string &field_name, const std::string &field_value_string)

Gets vertex by unique index. Throws exception if there is no such vertex.



参数

label_name – Name of the label.



field_name – Name of the field.



field_value_string – The field value string.



返回

The vertex by unique index.



VertexIterator GetVertexByUniqueCompositeIndex(const std::string &label_name, const std::vector<std::string> &field_name, const std::vector<std::string> &field_value_string)

OutEdgeIterator GetEdgeByUniqueIndex(const std::string &label_name, const std::string &field_name, const std::string &field_value_string)

Gets edge by unique index. Throws exception if there is no such vertex.



参数

label_name – Name of the label.



field_name – Name of the field.



field_value_string – The field value string.



返回

The vertex by unique index.



VertexIterator GetVertexByUniqueIndex(const std::string &label_name, const std::string &field_name, const FieldData &field_value)

Gets vertex by unique index. Throws exception if there is no such vertex.



参数

label_name – Name of the label.



field_name – Name of the field.



field_value – The field value.



返回

The vertex by unique index.



VertexIterator GetVertexByUniqueCompositeIndex(const std::string &label_name, const std::vector<std::string> &field_name, const std::vector<FieldData> &field_value)

OutEdgeIterator GetEdgeByUniqueIndex(const std::string &label_name, const std::string &field_name, const FieldData &field_value)

Gets edge by unique index. Throws exception if there is no such vertex.



参数

label_name – Name of the label.



field_name – Name of the field.



field_value – The field value.



返回

The vertex by unique index.



VertexIterator GetVertexByUniqueIndex(size_t label_id, size_t field_id, const FieldData &field_value)

Gets vertex by unique index. Throws exception if there is no such vertex.



参数

label_id – Identifier for the label.



field_id – Identifier for the field.



field_value – The field value.



返回

The vertex by unique index.



VertexIterator GetVertexByUniqueCompositeIndex(size_t label_id, const std::vector<size_t> &field_id, const std::vector<FieldData> &field_value)

OutEdgeIterator GetEdgeByUniqueIndex(size_t label_id, size_t field_id, const FieldData &field_value)

Gets edge by unique index. Throws exception if there is no such vertex.



参数

label_id – Identifier for the label.



field_id – Identifier for the field.



field_value – The field value.



返回

The vertex by unique index.



size_t GetNumVertices()

Gets the number of vertices.



返回

The nubmer of vertices.



const std::string &GetVertexPrimaryField(const std::string &label)

Gets vertex primary field



返回

The primary field.



std::pair<uint64_t, uint64_t> Count()

Get the total number of vertex and edge



返回

std::pair object, first element is vertex number, second is edge number.



std::vector<std::tuple<bool, std::string, int64_t>> CountDetail()

Get the total number of vertex or edge for each label



返回

std::tuple object list, first element indicates whether it is VERTEX or EDGE, second is label name, third is number.



Private Functions



explicit Transaction(lgraph::Transaction&&)

Private Members



std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class GraphDB

lgraph_types

namespace lgraph_api

Typedefs



typedef std::vector<std::pair<std::string, std::string>> EdgeConstraints

Edge constraints type define



Enums



enum class AccessLevel

Access level a user or role has on a graph. NONE: no permission. READ: read-only, no write access. WRITE: can read and write vertex and edge, but cannot change meta data such as schema or access. FULL: full access, can modify schema, grant access to other users, or even delete this graph.



Values:



enumerator NONE

enumerator READ

enumerator WRITE

enumerator FULL

enum class FieldAccessLevel

Values:



enumerator NONE

enumerator READ

enumerator WRITE

enum class GraphQueryType

Values:



enumerator CYPHER

enumerator GQL

enum FieldType

Field and value types.



Values:



enumerator NUL

enumerator NUL

enumerator NUL

enumerator BOOL

enumerator INT8

enumerator INT16

enumerator INT32

enumerator INT64

enumerator FLOAT

enumerator DOUBLE

enumerator DATE

enumerator DATETIME

enumerator STRING

enumerator BLOB

enumerator POINT

enumerator POINT

enumerator LINESTRING

enumerator LINESTRING

enumerator POLYGON

enumerator POLYGON

enumerator SPATIAL

enumerator FLOAT_VECTOR

enum class LGraphType : uint16_t

a type of value used in result entry and parameter in procedure or plugin signature



Param INTEGER

Param FLOAT

Param DOUBLE

Param BOOLEAN

Param STRING

Param MAP

<string, FieldData>



Param NODE

VertexIterator, VertexId



Param RELATIONSHIP

InEdgeIterator || OutEdgeIterator, EdgeUid



Param PATH

lgraph_api::Path



Param LIST

<string, FieldData>



Param ANY

like Object in Java, its procedure author’s responsibility to check the underlying concrete type whether valid in runtime.



Values:



enumerator NUL

enumerator INTEGER

enumerator FLOAT

enumerator DOUBLE

enumerator BOOLEAN

enumerator STRING

enumerator NODE

enumerator RELATIONSHIP

enumerator PATH

enumerator LIST

enumerator MAP

enumerator ANY

enum PluginCodeType

Type of code given when loading a new plugin.



Values:



enumerator PY

enumerator SO

enumerator CPP

enumerator ZIP

enum class IndexType

index type



Values:



enumerator NonuniqueIndex

this is not unique index



enumerator GlobalUniqueIndex

this is a global unique index



enumerator PairUniqueIndex

this is a pair unique index, for edge index only key of pair unique index is one of the follow case : if src_vid < dst_vid ,key is (index field value + src_vid + dst_vid) if src_vid > dst_vid ,key is (index field value + dst_vid + src_vid)



enum class CompositeIndexType

Values:



enumerator UniqueIndex

this is unique composite index



enumerator NonUniqueIndex

this is not unique composite index



Functions



static inline std::string to_string(const AccessLevel &v)

static inline std::string to_string(const FieldAccessLevel &v)

static inline std::string to_string(const GraphQueryType &v)

inline const std::string to_string(FieldType v)

Get the name of the given FieldType.



抛出

std::runtime_error – when an unrecognizable FieldType is given.



参数

v – A FieldType.



返回

Name of the given FieldType.



inline auto LGraphTypeIsField(LGraphType type) -> bool

inline auto LGraphTypeIsGraphElement(LGraphType type) -> bool

inline auto LGraphTypeIsCollection(LGraphType type) -> bool

inline auto LGraphTypeIsAny(LGraphType type) -> bool

inline const std::string to_string(LGraphType type)

inline std::string PluginCodeTypeStr(PluginCodeType code_type)

Get the name of plugin code types.



struct CompositeIndexSpec

#include <lgraph_types.h>

A composite index specifier.



Public Members



std::string label

label name



std::vector<std::string> fields

fields name



CompositeIndexType type

struct EdgeOptions : public LabelOptions

#include <lgraph_types.h>

Edge label options, contain fields only edge have



Public Types



enum class TemporalFieldOrder

Values:



enumerator ASC

enumerator DESC

Public Functions



EdgeOptions() = default

inline explicit EdgeOptions(const EdgeConstraints &edge_constraints)

inline virtual std::string to_string() const

inline virtual void clear()

Public Members



EdgeConstraints edge_constraints

std::string temporal_field

enum lgraph_api::EdgeOptions::TemporalFieldOrder temporal_field_order = TemporalFieldOrder::ASC

Public Static Functions



static inline std::string to_string(const TemporalFieldOrder &v)

struct EdgeUid

#include <lgraph_types.h>

Public Functions



inline EdgeUid()

inline EdgeUid(int64_t s, int64_t d, uint16_t l, int64_t t, int64_t e)

inline void Reverse()

Reverses side of this edge



inline bool operator==(const EdgeUid &rhs) const

inline bool operator!=(const EdgeUid &rhs) const

inline bool operator<(const EdgeUid &rhs) const

inline bool operator>(const EdgeUid &rhs) const

inline std::string ToString() const

Get string representation of this object



Public Members



int64_t src

source vertex id



int64_t dst

destination vertex id



uint16_t lid

label id



int64_t tid

timestamp



int64_t eid

additional edge id to distinguish edges with the same tid



Public Static Functions



static inline EdgeUid AnyEdge()

struct Hash

#include <lgraph_types.h>

Public Functions



inline size_t operator()(const EdgeUid &edgeUid) const

struct InEdgeSortOrder

#include <lgraph_types.h>

Comparator for EdgeUid of in-coming edges.



Public Functions



inline bool operator()(const EdgeUid &lhs, const EdgeUid &rhs) const

struct OutEdgeSortOrder

#include <lgraph_types.h>

Comparator for EdgeUid of out-going edges.



Public Functions



inline bool operator()(const EdgeUid &lhs, const EdgeUid &rhs) const

struct FieldData

#include <lgraph_types.h>

A class that represents variant type.



Public Functions



inline FieldData()

inline explicit FieldData(bool b)

inline explicit FieldData(int8_t integer)

inline explicit FieldData(int16_t integer)

inline explicit FieldData(int32_t integer)

inline explicit FieldData(int64_t integer)

inline explicit FieldData(float real)

inline explicit FieldData(double real)

inline explicit FieldData(const Date &d)

inline explicit FieldData(const DateTime &d)

inline explicit FieldData(const std::string &buf)

inline explicit FieldData(std::string &&str)

inline explicit FieldData(const char *buf)

inline explicit FieldData(const char *buf, size_t s)

inline explicit FieldData(const Point<Cartesian> &p)

inline explicit FieldData(const Point<Wgs84> &p)

inline explicit FieldData(const LineString<Cartesian> &l)

inline explicit FieldData(const LineString<Wgs84> &l)

inline explicit FieldData(const Polygon<Cartesian> &p)

inline explicit FieldData(const Polygon<Wgs84> &p)

inline explicit FieldData(const Spatial<Cartesian> &s)

inline explicit FieldData(const Spatial<Wgs84> &s)

inline explicit FieldData(const std::vector<float> &fv)

inline explicit FieldData(std::vector<float> &&fv)

inline ~FieldData()

inline FieldData(const FieldData &rhs)

inline FieldData(FieldData &&rhs)

inline FieldData &operator=(const FieldData &rhs)

inline FieldData &operator=(FieldData &&rhs)

inline int64_t integer() const

Access the FieldData as int64. Valid only when the FieldData is of INT8, INT16, INT32, or INT64 types.



抛出

std::bad_cast – Thrown when the FieldData is not of int types.



返回

An int64_t.



inline double real() const

Access the FieldData as a double. The FieldData must be of FLOAT or DOUBLE types.



抛出

std::bad_cast – Thrown if the FieldData is not of FLOAT or DOUBLE types.



返回

A double.



inline const std::string &string() const

Access the FieldData as std::string. Valid only for STRING, BLOB and SPATIAL. BLOB data is returned as-is, since std::string can also hold byte array.



抛出

std::bad_cast – Thrown when a bad cast error condition occurs.



返回

A reference to a const std::string.



inline bool AsBool() const

inline int8_t AsInt8() const

inline int16_t AsInt16() const

inline int32_t AsInt32() const

inline int64_t AsInt64() const

inline float AsFloat() const

inline double AsDouble() const

inline inline ::lgraph_api::Date AsDate () const

inline inline ::lgraph_api::DateTime AsDateTime () const

inline std::string AsString() const

inline std::string AsBlob() const

inline std::string AsBase64Blob() const

inline inline ::lgraph_api::SRID GetSRID () const

inline inline ::lgraph_api::Point<::lgraph_api::Wgs84 > AsWgsPoint () const

inline inline ::lgraph_api::Point<::lgraph_api::Cartesian > AsCartesianPoint () const

inline inline ::lgraph_api::LineString<::lgraph_api::Wgs84 > AsWgsLineString () const

inline inline ::lgraph_api::LineString<::lgraph_api::Cartesian > AsCartesianLineString () const

inline inline ::lgraph_api::Polygon<::lgraph_api::Wgs84 > AsWgsPolygon () const

inline inline ::lgraph_api::Polygon<::lgraph_api::Cartesian > AsCartesianPolygon () const

inline inline ::lgraph_api::Spatial<::lgraph_api::Wgs84 > AsWgsSpatial () const

inline inline ::lgraph_api::Spatial<::lgraph_api::Cartesian > AsCartesianSpatial () const

inline std::vector<float> AsFloatVector() const

std::any ToBolt() const

inline std::string ToString(const std::string &null_value = "NUL") const

Get string representation of this FieldData.



inline bool operator==(const FieldData &rhs) const

inline bool operator!=(const FieldData &rhs) const

inline bool operator>(const FieldData &rhs) const

inline bool operator>=(const FieldData &rhs) const

inline bool operator<(const FieldData &rhs) const

inline bool operator<=(const FieldData &rhs) const

inline FieldType GetType() const

inline bool is_null() const

inline bool is_buf() const

inline bool is_empty_buf() const

inline bool IsNull() const

Query if this object is null



inline bool IsBool() const

Query if this object is bool



inline bool IsBlob() const

Query if this object is BLOB



inline bool IsString() const

Query if this object is string



inline bool IsInt8() const

Query if this object is INT8



inline bool IsInt16() const

Query if this object is INT16



inline bool IsInt32() const

Query if this object is INT32



inline bool IsInt64() const

Query if this object is INT64



inline bool IsInteger() const

Is this a INT8, INT16, INT32 or INT64?



inline bool IsFloat() const

Query if this object is float



inline bool IsDouble() const

Query if this object is double



inline bool IsReal() const

Is this a FLOAT or DOUBLE?



inline bool IsDate() const

Query if this object is date



inline bool IsDateTime() const

Query if this object is date time



inline bool IsPoint() const

Query if this object is Point



inline bool IsLineString() const

Query if this object is LineString



inline bool IsPolygon() const

Query if this object is Polygon



inline bool IsSpatial() const

Query if this object is spatial



inline bool IsFloatVector() const

Query if this object is float vector



Public Members



FieldType type

bool boolean

int8_t int8

int16_t int16

int32_t int32

int64_t int64

float sp

double dp

std::string *buf

std::vector<float> *vp

union lgraph_api::FieldData::[anonymous] data

Public Static Functions



static inline FieldData Bool(bool b)

static inline FieldData Int8(int8_t i)

static inline FieldData Int16(int16_t i)

static inline FieldData Int32(int32_t i)

static inline FieldData Int64(int64_t i)

static inline FieldData Float(float d)

static inline FieldData Double(double d)

static inline FieldData Date(const std::string &str)

static inline FieldData Date(const ::lgraph_api::Date &d)

static inline FieldData DateTime(const std::string &str)

static inline FieldData DateTime(const ::lgraph_api::DateTime &d)

static inline FieldData String(const std::string &str)

static inline FieldData String(std::string &&str)

static inline FieldData String(const char *str)

static inline FieldData String(const char *p, size_t s)

static inline FieldData Point(const ::lgraph_api::Point<Cartesian> &p)

static inline FieldData Point(const ::lgraph_api::Point<Wgs84> &p)

static inline FieldData Point(const std::string &str)

static inline FieldData LineString(const ::lgraph_api::LineString<Cartesian> &l)

static inline FieldData LineString(const ::lgraph_api::LineString<Wgs84> &l)

static inline FieldData LineString(const std::string &str)

static inline FieldData Polygon(const ::lgraph_api::Polygon<Cartesian> &p)

static inline FieldData Polygon(const ::lgraph_api::Polygon<Wgs84> &p)

static inline FieldData Polygon(const std::string &str)

static inline FieldData Spatial(const ::lgraph_api::Spatial<Cartesian> &s)

static inline FieldData Spatial(const ::lgraph_api::Spatial<Wgs84> &s)

static inline FieldData Spatial(const std::string &str)

static inline FieldData FloatVector(const std::vector<float> &fv)

static inline FieldData Blob(const std::string &str)

static inline FieldData Blob(std::string &&str)

static inline FieldData Blob(const std::vector<uint8_t> &str)

Constructs a Blob from vector of uint8_t, treated as byte array.



static inline FieldData BlobFromBase64(const std::string &base64_encoded)

Constructs a BLOB from Base64 encoded string.



Private Static Functions



static inline bool IsBufType(FieldType t)

Query if ‘t’ is BLOB or STRING



static inline bool IsInteger(FieldType t)

Query if ‘t’ is INT8, 16, 32, or 64



static inline bool IsReal(FieldType t)

Query if ‘t’ is FLLOAT or DOUBLE



struct FieldSpec

#include <lgraph_types.h>

Specification for a field.



Public Functions



inline FieldSpec()

inline FieldSpec(const std::string &n, FieldType t, bool nu)

Constructor



参数

n – Field name



t – Field type



nu – True if field is optional



inline FieldSpec(std::string &&n, FieldType t, bool nu)

inline bool operator==(const FieldSpec &rhs) const

inline std::string ToString() const

Get the string representation of the FieldSpec.



Public Members



std::string name

name of the field



FieldType type

type of that field



bool optional

is this field optional?



struct IndexSpec

#include <lgraph_types.h>

An index specifier.



Public Members



std::string label

label name



std::string field

field name



IndexType type

struct LabelOptions

#include <lgraph_types.h>

Label options, base class, define some common fields and methods



Subclassed by EdgeOptions, VertexOptions



Public Functions



virtual std::string to_string() const = 0

virtual void clear() = 0

inline virtual ~LabelOptions()

Public Members



bool detach_property = false

struct Parameter

#include <lgraph_types.h>

The parameter of procedure/plugin



Public Members



std::string name

int index

name of the parameter



LGraphType type

index of the parameter list in which the parameter stay



struct RoleInfo

#include <lgraph_types.h>

Information about the role.



Public Members



std::string desc

description



std::map<std::string, AccessLevel> graph_access

access levels on different graphs



bool disabled = false

is this role disabled?



struct SigSpec

#include <lgraph_types.h>

Public Members



std::vector<Parameter> input_list

std::vector<Parameter> result_list

input parameter list



struct UserInfo

#include <lgraph_types.h>

Information about the user.



Public Members



std::string desc

description of the user



std::set<std::string> roles

roles of this user



bool disabled = false

is this user disabled?



size_t memory_limit

memory limit for this user



struct VectorIndexSpec

#include <lgraph_types.h>

Public Members



std::string label

std::string field

std::string index_type

int dimension

std::string distance_type

int hnsm_m

int hnsm_ef_construction

struct VertexOptions : public LabelOptions

#include <lgraph_types.h>

Vertex label options, contain fields only vertex have



Public Functions



VertexOptions() = default

inline explicit VertexOptions(const std::string &primary_field)

inline virtual std::string to_string() const

inline virtual void clear()

Public Members



std::string primary_field

lgraph_utils

Typedefs



using json = nlohmann::json

namespace lgraph_api

Functions



double get_time()

Get current time.



返回

Digit value of current time.



void split_string(std::string origin_string, std::vector<std::string> &sub_strings, std::string string_delimiter)

Split the original string by format.



参数

origin_string – original string to be split.



sub_strings – split substring.



string_delimiter – Split format.



std::string rc4(std::string &input, std::string key, std::string mode)

Encrypt the input string in ac4 format.



参数

input – input string.



key – encryption key.



mode – encryption mode



返回

Encrypted string



std::string encode_base64(const std::string input)

Encode the input string in encode_base64 format.



参数

input – input string.



返回

Encrypted string



std::string decode_base64(const std::string input)

Decode the input string in decode_base64 format.



参数

input – input string.



返回

Decrypted string.



void *alloc_buffer(size_t bytes)

Allocate memory with size in byte.



参数

bytes – Size in byte of request memory.



返回

Pointer of allocated memory.



void dealloc_buffer(void *buffer, size_t bytes)

Free memory with size in byte.



参数

buffer – Size in bytes of request memory



bytes – Pointer of memory to free.



template<class DataType>

void parse_from_json(DataType &value, const char *key, json &input)

Parse parameter from nlohmann::json.



参数

value – [out] value to store parameter



key – key of the parameter in the input



input – input json



template<class DataType>

void parse_from_json(std::vector<DataType> &value, const char *key, json &input)

Parse vector parameter from nlohmann::json.



参数

value – [out] value to store parameter



key – key of the parameter in the input



input – input json



size_t GetVidFromNodeString(const std::string &node_string)

Parse vid from the node passed in by cypher. For V2 procedure.



参数

node_string – [in] node



返回

vid



lgraph_vertex_index_iterator

namespace lgraph

namespace lgraph_api

class VertexIndexIterator

#include <lgraph_vertex_index_iterator.h>

VertexIndexIterator can be used to access a set of vertices that has the same indexed value. If the index is unique (that is, each vertex has a unique index value), then each VertexIndexIterator will only have one VertexId, and will become invalid after Next() is called.



An VertexIndexIterator is valid iff it points to a valid (index_value, vid) pair, otherwise it is invalid. Calling member function on an invalid VertexIndexIterator throws an exception, except for the IsValid() function.



Public Functions



VertexIndexIterator(VertexIndexIterator &&rhs)

VertexIndexIterator &operator=(VertexIndexIterator&&)

~VertexIndexIterator()

void Close()

Closes this iterator



bool IsValid() const

Query if this iterator is valid, i.e. the Key and Vid can be queried.



返回

True if valid, false if not.



bool Next()

Move to the next vertex id in the list, which consists of all the valid vertex ids of the iterator and is sorted from small to large. If we hit the end of the list, iterator will become invalid and false is returned.



返回

True if it succeeds, otherwise false.



FieldData GetIndexValue() const

Gets the current index value. The vids are sorted in (IndexValue, Vid) order. When Next() is called, the iterator moves from one vid to next, possibly moving from one IndexValue to another. This function tells the IndexValue currently pointed to.



返回

The key.



int64_t GetVid() const

Gets the current vertex id.



返回

The current vertex id.



Private Functions



VertexIndexIterator(lgraph::VertexIndexIterator &&it, const std::shared_ptr<lgraph::Transaction> &txn)

VertexIndexIterator(const VertexIndexIterator&) = delete

VertexIndexIterator &operator=(const VertexIndexIterator&) = delete

Private Members



std::unique_ptr<lgraph::VertexIndexIterator> it_

std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class Transaction

lgraph_vertex_iterator

namespace lgraph

namespace graph

namespace lgraph_api

class VertexIterator

#include <lgraph_vertex_iterator.h>

VertexIterator can be used to iterate through vertices in the DB. Vertices are sorted according to vertex id in the DB.



A VertexIterator is valid iff it points to a valid vertex. Calling method functions on an invalid VertexIterator throws an InvalidIterator, except for the IsValid() and Goto() functions.



The following operations invalidates a VertexIterator:



Constructing an VertexIterator for non-existing vertex.



Calling Goto() with the id of a non-existing vertex.



Calling Next() on the last vertex.



Calling Delete() on the last vertex.



Public Functions



VertexIterator(VertexIterator &&rhs)

VertexIterator &operator=(VertexIterator &&rhs)

~VertexIterator()

void Close()

Closes this iterator



bool Next()

Move to the next vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

True if it succeeds, otherwise return false (no more vertex) and invalidate the iterator.



bool Goto(int64_t vid, bool nearest = false)

Goto the vertex with id src. If there is no vertex with exactly the same vid, and nearest==true, go to the next vertex with id>=vid, otherwise return false and invalidate the iterator.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



参数

vid – Vertex id of the vertex to go.



nearest – (Optional) True to go to the closest vertex with id>=vid.



返回

True if it succeeds, otherwise false (no such vertex).



int64_t GetId() const

Gets the vertex id.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The id.



OutEdgeIterator GetOutEdgeIterator() const

Gets an OutEdgeIterator pointing to the first out-going edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The OutEdgeIterator.



OutEdgeIterator GetOutEdgeIterator(const EdgeUid &euid, bool nearest = false) const

Returns an OutEdgeIterator pointing to the edge specified by euid. If there is no such edge, and nearest==false an invalid iterator is returned. If the specified out-edge does not exist, and nearest==true, get the first out-edge that sorts after the specified one.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

euid – The Edge Unique Id.



nearest – (Optional) If set to true and the specified edge does not exist, get the edge that sorts right after it.



返回

The out edge iterator.



InEdgeIterator GetInEdgeIterator() const

Gets an InEdgeIterator pointing to the first in-coming edge.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The InEdgeIterator.



InEdgeIterator GetInEdgeIterator(const EdgeUid &euid, bool nearest = false) const

Returns an InEdgeIterator pointing to the edge specified by euid. If there is no such edge and nearest==false, an invalid iterator is returned. If the specified edge does not exist and nearest==true,



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

euid – The Edge Unique Id.



nearest – (Optional) If set to true and the specified edge does not exist, get the edge that sorts right after it.



返回

The InEdgeIterator.



bool IsValid() const

Query if this iterator is valid.



返回

True if valid, false if not.



const std::string &GetLabel() const

Gets the label of this vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The label.



size_t GetLabelId() const

Gets label id of this vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

The label identifier.



std::vector<FieldData> GetFields(const std::vector<std::string> &field_names) const

Gets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



返回

The fields.



FieldData GetField(const std::string &field_name) const

Gets the field specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – Field name.



返回

Field value.



std::vector<FieldData> GetFields(const std::vector<size_t> &field_ids) const

Gets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_ids – List of ids for the fields.



返回

The fields.



FieldData GetField(size_t field_id) const

Gets the field specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_id – Field ID.



返回

Field value.



inline FieldData operator[](const std::string &field_name) const

Get field identified by field_name



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – Filename of the file.



返回

The indexed value.



inline FieldData operator[](size_t fid) const

Get field identified by field id



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



InputError – Thrown on other input errors (field not exist, etc.).



参数

fid – The field id.



返回

The indexed value.



std::map<std::string, FieldData> GetAllFields() const

Gets all fields of current vertex.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



返回

all fields.



void SetField(const std::string &field_name, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_name – Field name.



field_value – Field value.



void SetField(size_t field_id, const FieldData &field_value)

Sets the specified field.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_id – Field id.



field_value – Field value.



void SetFields(const std::vector<std::string> &field_names, const std::vector<std::string> &field_value_strings)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



field_value_strings – The field value strings.



void SetFields(const std::vector<std::string> &field_names, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_names – List of names of the fields.



field_values – The field values.



void SetFields(const std::vector<size_t> &field_ids, const std::vector<FieldData> &field_values)

Sets the fields specified.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



InputError – Thrown on other input errors (field not exist, etc.).



参数

field_ids – List of identifiers for the fields.



field_values – The field values.



std::vector<int64_t> ListSrcVids(size_t n_limit = std::numeric_limits<size_t>::max(), bool *more_to_go = nullptr)

List source vids. Each source vid is stored only once in the result.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

n_limit – (Optional) The limit on number of vids to return.



more_to_go – [out] (Optional) If non-null, returns whether the limit is exceeded.



返回

List of source vids.



std::vector<int64_t> ListDstVids(size_t n_limit = std::numeric_limits<size_t>::max(), bool *more_to_go = nullptr)

List destination vids. Each vid is stored only once in the result.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

n_limit – (Optional) The limit of number of vids to return.



more_to_go – [out] (Optional) If non-null, returns whether the limit is exceeded.



返回

List of desitnation vids.



size_t GetNumInEdges(size_t n_limit = std::numeric_limits<size_t>::max(), bool *more_to_go = nullptr)

Gets number of incoming edges, stopping on limit. This function can come in handy if we need to filter on large vertexes.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

n_limit – (Optional) The limit on number of in-coming edges to count. When the limit is reached, n_limit is returned.



more_to_go – [out] (Optional) If non-null, return whether the limit is exceeded.



返回

Number of incoming edges.



size_t GetNumOutEdges(size_t n_limit = std::numeric_limits<size_t>::max(), bool *more_to_go = nullptr)

Gets number of out-going edges, stopping on limit. This function can come in handy if we need to filter on large vertexes.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



参数

n_limit – (Optional) The limit on number of out-going edges to count. When the limit is reached, n_limit is returned and limit_exceeded is set to true.



more_to_go – [out] (Optional) If non-null, return whether the limit is exceeded.



返回

Number of out-going edges.



void Delete(size_t *n_in_edges = nullptr, size_t *n_out_edges = nullptr)

Deletes this vertex, also deletes all incoming and outgoing edges of this vertex. The iterator will point to the next vertex by vid if there is any.



抛出

InvalidTxn – Thrown when called inside an invalid transaction.



InvalidIterator – Thrown when current iterator is invalid.



WriteNotAllowed – Thrown when called in a read-only transaction.



参数

n_in_edges – [out] (Optional) If non-null, the number of in edges the vertex had.



n_out_edges – [out] (Optional) If non-null, the number of out edges the vertex had.



std::string ToString() const

Get the string representation of this vertex.



Private Functions



VertexIterator(lgraph::graph::VertexIterator&&, const std::shared_ptr<lgraph::Transaction>&)

VertexIterator(const VertexIterator&) = delete

VertexIterator &operator=(const VertexIterator&) = delete

Private Members



std::unique_ptr<lgraph::graph::VertexIterator> it_

std::shared_ptr<lgraph::Transaction> txn_

Friends



friend class Transaction

olap_base

This is an implementation of the TuGraph graph analytics engine. The graph analytics engine is a general-purpose processing engine useful for implementing various graph analytics algorithms such as PageRank, ShortestPath, etc..



Defines



THREAD_WORKING

THREAD_STEALING

VERTEX_BATCH_SIZE

WORD_OFFSET(i)

BIT_OFFSET(i)

Functions



union @5 __attribute__ ((packed))

Variables



size_t neighbour

EdgeData edge_data

size_t src

size_t dst

namespace lgraph_api

namespace olap

Enums



enum EdgeDirectionPolicy

Define the edge direction policy of graph The policy determines the graph symmetric and undirected feature.



Values:



enumerator DUAL_DIRECTION

The graph is asymmetric. The edges from input files are outgoing edges. The reversed edges form incoming edges.



enumerator MAKE_SYMMETRIC

The graph is symmetric but the input files are asymmetric. The outgoing and incoming edges are identical.



enumerator INPUT_SYMMETRIC

Both the graph and the input files are symmetric. The outgoing and incoming edges are identical.



Functions



template<typename EdgeData> struct lgraph_api::olap::AdjUnit __attribute__ ((packed))

template<> struct lgraph_api::olap::AdjUnit< Empty > __attribute__ ((packed))

template<typename ReducedSum>

static ReducedSum reduce_plus(ReducedSum a, ReducedSum b)

The default reduce function which uses the plus operator.



template<typename T>

T ForEachVertex(GraphDB &db, Transaction &txn, std::vector<Worker> &workers, const std::vector<int64_t> &vertices, std::function<void(Transaction&, VertexIterator&, T&)> work, std::function<void(const T&, T&)> reduce, size_t parallel_factor = 8)

template<typename T>

std::vector<T> ForEachVertex(GraphDB &db, Transaction &txn, std::vector<Worker> &workers, const std::vector<int64_t> &vertices, std::function<T(Transaction&, VertexIterator&, size_t)> work, size_t parallel_factor = 8)

Variables



struct lgraph_api::olap::EdgeStringUnit __attribute__

static constexpr size_t MAX_NUM_EDGES = 1ul << 36

The maximum number of edges. Change this value if needed.



template<typename EdgeData>

class AdjList

#include <olap_base.h>

Public Functions



inline AdjList()

inline AdjUnit<EdgeData> *begin()

inline AdjUnit<EdgeData> *end()

inline AdjUnit<EdgeData> &operator[](size_t i)

Private Functions



inline AdjList(AdjUnit<EdgeData> *begin, AdjUnit<EdgeData> *end)

Private Members



AdjUnit<EdgeData> *begin_

AdjUnit<EdgeData> *end_

Friends



friend class OlapBase< EdgeData >

template<typename EdgeData>

struct AdjUnit

#include <olap_base.h>

AdjUnit<EdgeData> represents an adjacent edge with EdgeData as the weight type.



模板参数

EdgeData – Type of the edge data.



Public Members



size_t neighbour

EdgeData edge_data

template<>

struct AdjUnit<Empty>

#include <olap_base.h>

Public Functions



template<> union lgraph_api::olap::AdjUnit< Empty >::@4 __attribute__ ((packed))

Public Members



size_t neighbour

Empty edge_data

template<typename EdgeData>

struct EdgeStringUnit

#include <olap_base.h>

EdgeStringUnit<EdgeData> represents an edge with EdgeData as the weight type, The vertex is of string type.



模板参数

EdgeData – Type of the edge data.



Public Members



std::string src

std::string dst

EdgeData edge_data

template<typename EdgeData>

struct EdgeUnit

#include <olap_base.h>

EdgeUnit<EdgeData> represents an edge with EdgeData as the weight type.



模板参数

EdgeData – Type of the edge data.



Public Members



size_t src

size_t dst

EdgeData edge_data

template<>

struct EdgeUnit<Empty>

#include <olap_base.h>

Public Functions



template<> union lgraph_api::olap::EdgeUnit< Empty >::@6 __attribute__ ((packed))

Public Members



size_t src

size_t dst

Empty edge_data

struct Empty

#include <olap_base.h>

Empty is used for representing unweighted graphs.



template<typename EdgeData>

class OlapBase

#include <olap_base.h>

AdjList<EdgeData> allows range-based for-loop over AdjUnit<EdgeData>.



Graph



EdgeData is used for representing edge weights (the default type is Empty which is used for unweighted graphs).



模板参数

EdgeData – Type of the edge data.



EdgeData – Graph instances represent static (sub)graphs loaded from txt file. The internal organization uses compressed sparse matrix formats which are optimized for read-only accesses.



EdgeData – Type of the edge data.



Subclassed by OlapOnDB< EdgeData >



Public Functions



inline OlapBase()

Constructor of Graph.



inline virtual bool CheckKillThisTask()

inline size_t OutDegree(size_t vid)

Access the out-degree of some vertex.



参数

vid – The vertex id (in the Graph) to access.



返回

The out-degree of the specified vertex in the Graph.



inline size_t InDegree(size_t vid)

Access the in-degree of some vertex.



参数

vid – The vertex id (in the Graph) to access.



返回

The in-degree of the specified vertex in the Graph.



inline AdjList<EdgeData> OutEdges(size_t vid)

Access the outgoing edges of some vertex.



参数

vid – The vertex id (in the Graph) to access.



返回

The outgoing edges of the specified vertex in the Graph.



inline AdjList<EdgeData> InEdges(size_t vid)

Access the incoming edges of some vertex.



参数

vid – The vertex id (in the Graph) to access.



返回

The incoming edges of the specified vertex in the Graph.



inline void Transpose()

Transpose the graph.



inline size_t NumVertices()

Get number of vertices of the Graph.



返回

Number of vertices of the Graph.



inline size_t NumEdges()

Get number of edges of the Graph.



返回

Number of edges of the Graph.



template<typename VertexData>

inline ParallelVector<VertexData> AllocVertexArray()

Allocate a vertex array with type VertexData.



模板参数

VertexData – Type of the vertex data.



返回

A ParallelVector with type VertexData.



inline ParallelBitset AllocVertexSubset()

Allocate a vertex subset represented with ParallelBitset.



返回

A ParallelBitset sized |V| of the Graph.



inline void AcquireVertexLock(size_t vid)

Lock some vertex to ensure correct concurrent updates.



参数

vid – The vertex id (in the Graph) to lock.



inline void ReleaseVertexLock(size_t vid)

Unlock some vertex to ensure correct concurrent updates.



参数

vid – The vertex id (in the Graph) to unlock.



inline VertexLockGuard GuardVertexLock(size_t vid)

Get a VertexLockGuard of some vertex.



参数

vid – The vertex id (in the Graph) to lock/unlock.



返回

A VertexLockGuard corresponding to the specified vertex.



inline bool IfSparse(ParallelBitset &active_vertices)

Judging whether it is sparse mode or dense mode according to the number of vertices.



参数

active_vertices – The ParallelBitset of active_vertices.



inline void set_num_vertices(size_t vertices)

Assign vertices to the first loaded graph.



参数

vertices – The vertex id (in the Graph) to lock/unlock.



inline void LoadFromArray(char *edge_array, size_t input_vertices, size_t input_edges, EdgeDirectionPolicy edge_direction_policy)

Load graph data from edge_array.



参数

edge_array – [in] The data in this array is read into the graph.



input_vertices – The number of vertices in the input graph data.



input_edges – The number of edges in the input graph data.



edge_direction_policy – Graph data loading method.



template<typename ReducedSum>

inline ReducedSum ProcessVertexInRange(std::function<ReducedSum(size_t)> work, size_t lower, size_t upper, ReducedSum zero = 0, std::function<ReducedSum(ReducedSum, ReducedSum)> reduce = reduce_plus<ReducedSum>)

Execute a parallel-for loop in the range [lower, upper).



抛出

std::runtime_error – Raised when a runtime error condition occurs.



模板参数

ReducedSum – Type of the reduced sum.



参数

work – The function describing the work.



lower – The lower bound of the range (inclusive).



upper – The upper bound of the range (exclusive).



zero – (Optional) The initial value for reduction.



reduce – (Optional) The function describing the reduction logic.



返回

A reduction value.



template<typename ReducedSum, typename Algorithm>

inline ReducedSum ProcessVertexInRange(std::function<ReducedSum(Algorithm, size_t)> work, size_t lower, size_t upper, Algorithm algorithm, ReducedSum zero = 0, std::function<ReducedSum(ReducedSum, ReducedSum)> reduce = reduce_plus<ReducedSum>)

template<typename ReducedSum>

inline ReducedSum ProcessVertexActive(std::function<ReducedSum(size_t)> work, ParallelBitset &active_vertices, ReducedSum zero = 0, std::function<ReducedSum(ReducedSum, ReducedSum)> reduce = reduce_plus<ReducedSum>)

Process a set of active vertices in parallel.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



模板参数

ReducedSum – Type of the reduced sum.



参数

work – The function describing each vertex’s work.



active_vertices – [inout] The active vertex set.



zero – (Optional) The initial value for reduction.



reduce – (Optional) The function describing the reduction logic.



返回

A reduction value.



template<typename ReducedSum, typename Algorithm>

inline ReducedSum ProcessVertexActive(std::function<ReducedSum(Algorithm, size_t)> work, ParallelBitset &active_vertices, Algorithm algorithm, ReducedSum zero = 0, std::function<ReducedSum(ReducedSum, ReducedSum)> reduce = reduce_plus<ReducedSum>)

Protected Functions



inline virtual void Construct()

Protected Attributes



size_t num_vertices_

size_t num_edges_

size_t edge_data_size_

size_t adj_unit_size_

size_t edge_unit_size_

EdgeDirectionPolicy edge_direction_policy_

EdgeUnit<EdgeData> *edge_list_

ParallelVector<size_t> out_degree_

ParallelVector<size_t> in_degree_

ParallelVector<size_t> out_index_

ParallelVector<size_t> in_index_

ParallelVector<AdjUnit<EdgeData>> out_edges_

ParallelVector<AdjUnit<EdgeData>> in_edges_

ParallelVector<bool> lock_array_

class ParallelBitset

#include <olap_base.h>

ParallelBitset implements the concurrent bitset data structure, which is usually used to represent active vertex sets.



Public Functions



explicit ParallelBitset(size_t size)

Construct a ParallelBitset.



参数

size – The size of the bitset (i.e. the number of bits).



ParallelBitset(const ParallelBitset &rhs) = delete

inline ParallelBitset &operator=(ParallelBitset &&rhs)

inline ParallelBitset(ParallelBitset &&rhs)

inline ParallelBitset()

~ParallelBitset()

void Clear()

Clear the bitset.



void Fill()

Fill the bitset.



bool Has(size_t i)

Test a specified bit.



参数

i – The bit to test.



返回

Whether the bit is set or not.



bool Add(size_t i)

Set a specified bit.



参数

i – The bit to set.



返回

Whether the operation is a true addition or not.



void Swap(ParallelBitset &other)

Swap the current bitset with another one.



参数

other – [inout] The other bitset to swap with.



inline uint64_t *Data()

inline size_t Size()

Private Members



uint64_t *data_

size_t size_

template<typename T>

class ParallelVector

#include <olap_base.h>

ParallelVector<T> aims to mimic std::vector<T>. Note that the deletions other than clearing are not supported.



Public Functions



inline explicit ParallelVector(size_t capacity)

Construct a ParallelVector<T>.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

capacity – The capacity of the vector.



inline explicit ParallelVector(size_t capacity, size_t size)

Construct a ParallelVector<T>.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

capacity – The capacity of the vector.



size – The initial size of the vector.



inline ParallelVector(T *data, size_t size)

Construct a ParallelVector<T>



参数

data – The initial data of the vector.



size – The initial size of the vector. And the initial capacity equals initial size.



ParallelVector(const ParallelVector<T> &rhs) = delete

inline ParallelVector(ParallelVector<T> &&rhs)

inline ParallelVector<T> &operator=(ParallelVector<T> &&rhs)

inline ParallelVector()

Default constructor of ParallelVector<T>.



inline void Destroy()

Destroy ParallelVector<T>.



inline ~ParallelVector()

inline T &operator[](size_t i)

inline T *begin()

inline T *end()

inline T &Back()

inline T *Data()

inline size_t Size()

inline size_t Capacity()

inline bool Destroyed()

inline void Resize(size_t size)

Change ParallelVector size. Note the new size should be larger than or equal to elder size.



参数

size – Value of new size.



inline void Resize(size_t size, const T &elem)

Change ParallelVector size and initialize the new element with elem. Note the new size should be larger than or equal to elder size.



参数

size – Value of new size.



elem – Initial value of new-added element.



inline void Clear()

Clear all data and change size to 0.



inline void ReAlloc(size_t capacity)

Destroy elder data and allocate with new capacity.



参数

capacity – New capacity value.



inline void Fill(T elem)

Assign the vector’s elements with a common value.



参数

elem – The common value.



     This action is performed in parallel, so you should not call

     it inside another parallel region (via Worker::Delegate).

inline void Append(const T &elem, bool atomic = true)

Append an element to the vector.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

elem – The element.



atomic – (Optional) Whether atomic instructions should be used or not.



inline void Append(T *buf, size_t count, bool atomic = true)

Append an array of elements to the vector.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

buf – [inout] The array pointer.



count – The array length.



atomic – (Optional) True to atomic.



inline void Append(ParallelVector<T> &other, bool atomic = true)

Append another vector of elements to this.



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

other – [inout] The other vector.



atomic – (Optional) True to atomic.



inline void Swap(ParallelVector<T> &other)

Swap the current vector with another one.



参数

other – [inout] The other vector to swap with.



inline ParallelVector<T> Copy()

Copy the current vector.



返回

A new vector with the same copied content.



Private Members



bool destroyed_

size_t capacity_

T *data_

size_t size_

struct ThreadState

#include <olap_base.h>

Public Members



size_t curr

size_t end

int state

class VertexLockGuard

#include <olap_base.h>

The VertexLockGuard automatically acquires the lock on construction and releases the lock on destruction.



Public Functions



explicit VertexLockGuard(volatile bool *lock)

VertexLockGuard(const VertexLockGuard &rhs) = delete

VertexLockGuard(VertexLockGuard &&rhs) = default

~VertexLockGuard()

Private Members



bool *lock_

class Worker

#include <olap_base.h>

All the parallel tasks should be delegated through Worker to prevent a huge number of threads being populated via OpenMP.



Public Functions



Worker()

~Worker()

void Delegate(const std::function<void()> &work)

Send some work to the Worker instance.



参数

work – The function describing the work.



             Exceptions can be thrown in the work function if necessary.

             Note that Delegate cannot be nested.

template<typename Compute>

inline void DelegateCompute(const std::function<void(Compute&)> &work, Compute &compute)

Public Static Functions



static std::shared_ptr<Worker> &SharedWorker()

Get the global (shared) worker.



返回

A shared pointer to the global Worker instance.



Private Members



bool stopping_

bool has_work_

std::mutex mutex_

std::condition_variable cv_

std::shared_ptr<std::packaged_task<void()>> task_

std::thread worker_

olap_on_db

TuGraph OLAP interface. To implement a plugin that perform graph analytics on TuGraph, user can load a Snapshot from the database, and then use the Gather-Apply-Scatter style interface to do the computation.



namespace lgraph_api

namespace olap

Variables



static constexpr size_t SNAPSHOT_PARALLEL = 1ul << 0

The available options for (graph construction) flags.



static constexpr size_t SNAPSHOT_UNDIRECTED = 1ul << 1

static constexpr size_t SNAPSHOT_IDMAPPING = 1ul << 2

static constexpr size_t SNAPSHOT_OUT_DEGREE = 1ul << 3

The following options are not implemented yet.



static constexpr size_t SNAPSHOT_IN_DEGREE = 1ul << 4

static constexpr size_t SNAPSHOT_OUT_EDGES = 1ul << 5

static constexpr size_t SNAPSHOT_IN_EDGES = 1ul << 6

template<typename EdgeData>

std::function<bool(OutEdgeIterator&, EdgeData&)> edge_convert_default = [](OutEdgeIterator &eit, EdgeData &edge_data) -> bool {     edge_data= 1;return true;}

Default Parser for weighted edges for graph.



Return

Edge is converted into graph or not.



template<typename EdgeData>

std::function<bool(OutEdgeIterator&, EdgeData&)> edge_convert_weight = [](OutEdgeIterator &eit, EdgeData &edge_data) -> bool {     edge_data= eit.GetField("weight").real();return true;}

Example parser for extract from edge property “weight”



Return

Edge is converted into graph or not.



template<typename EdgeData>

class OlapOnDB : public lgraph_api::olap::OlapBase<EdgeData>

#include <olap_on_db.h>

Snapshot is a derived class of Graph. Snapshot instances represent static (sub)graphs exported from LightningGraph. The internal organization uses compressed sparse matrix formats which are optimized for read-only accesses.



EdgeData is used for representing edge weights (the default type is Empty which is used for unweighted graphs).



模板参数

EdgeData – Type of the edge data.



Public Functions



inline OlapOnDB(GraphDB *db, Transaction &txn, size_t flags = 0, std::function<bool(VertexIterator&)> vertex_filter = nullptr, std::function<bool(OutEdgeIterator&, EdgeData&)> out_edge_filter = nullptr)

Generate a graph with LightningGraph. For V1/V2 Procedures



inline OlapOnDB(GraphDB &db, Transaction &txn, size_t flags = 0, std::function<bool(VertexIterator&)> vertex_filter = nullptr, std::function<bool(OutEdgeIterator&, EdgeData&)> out_edge_filter = nullptr)

Generate a graph with LightningGraph. For V1 Procedures



Note: read-write transactions are not recommended here for safety, e.g. some vertices might be removed causing inconsistencies of the analysis, and vertex data extraction may not work for deleted vertices). The constructed graph should contain all vertices whose vertex_filter calls return true and all edges sourced from these vertices whose out_edge_filter calls return true. If SNAPSHOT_UNDIRECTED is specified, the graph will be made symmetric (i.e. reversed edges are also added to the graph).



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

db – [inout] The GraphDB instance.



txn – [inout] The transaction.



flags – (Optional) The generation flags.



vertex_filter – [inout] (Optional) A function filtering vertices.



out_edge_filter – [inout] (Optional) A function filtering out edges.



inline OlapOnDB(GraphDB &db, Transaction &txn, std::vector<std::vector<std::string>> label_list, size_t flags = 0)

inline OlapOnDB(Transaction &txn, size_t flags = 0, std::function<bool(VertexIterator&)> vertex_filter = nullptr, std::function<bool(OutEdgeIterator&, EdgeData&)> out_edge_filter = nullptr)

Generate a graph without LightningGraph. For V2 Procedures



抛出

std::runtime_error – Raised when a runtime error condition occurs.



参数

txn – [inout] The transaction.



flags – (Optional) The generation flags.



vertex_filter – [inout] (Optional) A function filtering vertices.



out_edge_filter – [inout] (Optional) A function filtering out edges.



OlapOnDB() = delete

OlapOnDB(const OlapOnDB<EdgeData> &rhs) = delete

OlapOnDB(OlapOnDB<EdgeData> &&rhs) = default

inline OlapOnDB<EdgeData> &operator=(OlapOnDB<EdgeData> &&rhs)

inline virtual ~OlapOnDB()

template<typename VertexData>

inline ParallelVector<VertexData> ExtractVertexData(std::function<void(VertexIterator&, VertexData&)> extract)

Extract a vertex array from the graph.



参数

extract – The function describing the extraction logic.



返回

A ParallelVector containing each vertex’s extracted data.



template<typename VertexData>

inline void WriteToFile(ParallelVector<VertexData> &vertex_data, const std::string &output_file, std::function<bool(size_t vid, VertexData &vdata)> output_filter = nullptr)

Write vertex data to a file.



参数

vertex_data – The parallel vector storing the vertex data.



output_file – The path to the output file.



template<typename VertexData>

inline void WriteToFile(bool detail_output, ParallelVector<VertexData> &vertex_data, const std::string &output_file, std::function<bool(size_t vid, VertexData &vdata)> output_filter = nullptr)

Write vertex data(include label、primary_field、field_data) to a file.



参数

detail_output – always true



vertex_data – The parallel vector storing the vertex data.



output_file – The path to the output file.



template<typename VertexData>

inline void WriteToGraphDB(ParallelVector<VertexData> &vertex_data, const std::string &vertex_field)

Write vertex data to the graph database.



参数

vertex_data – [inout] The parallel vector storing the vertex data.



vertex_field – [in] The name of the vertex field.



inline int64_t OriginalVid(size_t vid)

Get the original vertex id (in LightningGraph) of some vertex.



参数

vid – The vertex id (in the graph) to access.



返回

The original id of the specified vertex in the graph.



inline size_t MappedVid(size_t original_vid)

Get the mapped vertex id (in the graph) of some vertex.



参数

original_vid – The original vertex id (in LightningGraph) to access.



返回

The mapped id of the specified vertex (in LightningGraph).



inline Transaction &GetTransaction()

Private Functions



inline void Init(size_t num_vertices)

inline virtual bool CheckKillThisTask()

This decision formula is used to determine whether to stop the algorithm running in OlapOnDB.



inline virtual void Construct()

inline void ConstructWithVid()

inline void ConstructWithDegree()

Private Members



GraphDB *db_

Transaction &txn_

ParallelVector<size_t> original_vids_

cuckoohash_map<size_t, size_t> vid_map_

size_t flags_

std::function<bool(VertexIterator&)> vertex_filter_

std::function<bool(OutEdgeIterator&, EdgeData&)> out_edge_filter_

olap_profile

namespace lgraph_api

namespace olap

class MemUsage

#include <olap_profile.h>

Public Functions



inline MemUsage()

inline int64_t getMaxMemUsage()

void reset()

void startMemRecord(unsigned int interval = 1000)

void print()

Private Functions



int parseMemLine(char *line)

Private Members



size_t maxMemUsage

