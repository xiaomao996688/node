# Copyright 2019 the V8 project authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can
# be found in the LICENSE file.

# This file is automatically generated by mkgrokdump and should not
# be modified manually.

# List of known V8 instance types.
INSTANCE_TYPES = {
  0: "INTERNALIZED_STRING_TYPE",
  2: "EXTERNAL_INTERNALIZED_STRING_TYPE",
  8: "ONE_BYTE_INTERNALIZED_STRING_TYPE",
  10: "EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  18: "UNCACHED_EXTERNAL_INTERNALIZED_STRING_TYPE",
  26: "UNCACHED_EXTERNAL_ONE_BYTE_INTERNALIZED_STRING_TYPE",
  32: "STRING_TYPE",
  33: "CONS_STRING_TYPE",
  34: "EXTERNAL_STRING_TYPE",
  35: "SLICED_STRING_TYPE",
  37: "THIN_STRING_TYPE",
  40: "ONE_BYTE_STRING_TYPE",
  41: "CONS_ONE_BYTE_STRING_TYPE",
  42: "EXTERNAL_ONE_BYTE_STRING_TYPE",
  43: "SLICED_ONE_BYTE_STRING_TYPE",
  45: "THIN_ONE_BYTE_STRING_TYPE",
  50: "UNCACHED_EXTERNAL_STRING_TYPE",
  58: "UNCACHED_EXTERNAL_ONE_BYTE_STRING_TYPE",
  64: "SYMBOL_TYPE",
  65: "BIG_INT_BASE_TYPE",
  66: "HEAP_NUMBER_TYPE",
  67: "ODDBALL_TYPE",
  68: "ABSTRACT_INTERNAL_CLASS_SUBCLASS1_TYPE",
  69: "ABSTRACT_INTERNAL_CLASS_SUBCLASS2_TYPE",
  70: "FOREIGN_TYPE",
  71: "WASM_TYPE_INFO_TYPE",
  72: "PROMISE_FULFILL_REACTION_JOB_TASK_TYPE",
  73: "PROMISE_REJECT_REACTION_JOB_TASK_TYPE",
  74: "CALLABLE_TASK_TYPE",
  75: "CALLBACK_TASK_TYPE",
  76: "PROMISE_RESOLVE_THENABLE_JOB_TASK_TYPE",
  77: "LOAD_HANDLER_TYPE",
  78: "STORE_HANDLER_TYPE",
  79: "FUNCTION_TEMPLATE_INFO_TYPE",
  80: "OBJECT_TEMPLATE_INFO_TYPE",
  81: "ACCESS_CHECK_INFO_TYPE",
  82: "ACCESSOR_INFO_TYPE",
  83: "ACCESSOR_PAIR_TYPE",
  84: "ALIASED_ARGUMENTS_ENTRY_TYPE",
  85: "ALLOCATION_MEMENTO_TYPE",
  86: "ALLOCATION_SITE_TYPE",
  87: "ARRAY_BOILERPLATE_DESCRIPTION_TYPE",
  88: "ASM_WASM_DATA_TYPE",
  89: "ASYNC_GENERATOR_REQUEST_TYPE",
  90: "BREAK_POINT_TYPE",
  91: "BREAK_POINT_INFO_TYPE",
  92: "CACHED_TEMPLATE_OBJECT_TYPE",
  93: "CALL_HANDLER_INFO_TYPE",
  94: "CLASS_POSITIONS_TYPE",
  95: "DEBUG_INFO_TYPE",
  96: "ENUM_CACHE_TYPE",
  97: "FEEDBACK_CELL_TYPE",
  98: "FUNCTION_TEMPLATE_RARE_DATA_TYPE",
  99: "INTERCEPTOR_INFO_TYPE",
  100: "INTERPRETER_DATA_TYPE",
  101: "MODULE_REQUEST_TYPE",
  102: "PROMISE_CAPABILITY_TYPE",
  103: "PROMISE_REACTION_TYPE",
  104: "PROPERTY_DESCRIPTOR_OBJECT_TYPE",
  105: "PROTOTYPE_INFO_TYPE",
  106: "SCRIPT_TYPE",
  107: "SOURCE_TEXT_MODULE_INFO_ENTRY_TYPE",
  108: "STACK_FRAME_INFO_TYPE",
  109: "STACK_TRACE_FRAME_TYPE",
  110: "TEMPLATE_OBJECT_DESCRIPTION_TYPE",
  111: "TUPLE2_TYPE",
  112: "WASM_EXCEPTION_TAG_TYPE",
  113: "WASM_EXPORTED_FUNCTION_DATA_TYPE",
  114: "WASM_INDIRECT_FUNCTION_TABLE_TYPE",
  115: "WASM_JS_FUNCTION_DATA_TYPE",
  116: "WASM_VALUE_TYPE",
  117: "FIXED_ARRAY_TYPE",
  118: "HASH_TABLE_TYPE",
  119: "EPHEMERON_HASH_TABLE_TYPE",
  120: "GLOBAL_DICTIONARY_TYPE",
  121: "NAME_DICTIONARY_TYPE",
  122: "NUMBER_DICTIONARY_TYPE",
  123: "ORDERED_HASH_MAP_TYPE",
  124: "ORDERED_HASH_SET_TYPE",
  125: "ORDERED_NAME_DICTIONARY_TYPE",
  126: "SIMPLE_NUMBER_DICTIONARY_TYPE",
  127: "CLOSURE_FEEDBACK_CELL_ARRAY_TYPE",
  128: "OBJECT_BOILERPLATE_DESCRIPTION_TYPE",
  129: "SCOPE_INFO_TYPE",
  130: "SCRIPT_CONTEXT_TABLE_TYPE",
  131: "BYTE_ARRAY_TYPE",
  132: "BYTECODE_ARRAY_TYPE",
  133: "FIXED_DOUBLE_ARRAY_TYPE",
  134: "INTERNAL_CLASS_WITH_SMI_ELEMENTS_TYPE",
  135: "SLOPPY_ARGUMENTS_ELEMENTS_TYPE",
  136: "AWAIT_CONTEXT_TYPE",
  137: "BLOCK_CONTEXT_TYPE",
  138: "CATCH_CONTEXT_TYPE",
  139: "DEBUG_EVALUATE_CONTEXT_TYPE",
  140: "EVAL_CONTEXT_TYPE",
  141: "FUNCTION_CONTEXT_TYPE",
  142: "MODULE_CONTEXT_TYPE",
  143: "NATIVE_CONTEXT_TYPE",
  144: "SCRIPT_CONTEXT_TYPE",
  145: "WITH_CONTEXT_TYPE",
  146: "EXPORTED_SUB_CLASS_BASE_TYPE",
  147: "EXPORTED_SUB_CLASS_TYPE",
  148: "EXPORTED_SUB_CLASS2_TYPE",
  149: "SMALL_ORDERED_HASH_MAP_TYPE",
  150: "SMALL_ORDERED_HASH_SET_TYPE",
  151: "SMALL_ORDERED_NAME_DICTIONARY_TYPE",
  152: "DESCRIPTOR_ARRAY_TYPE",
  153: "STRONG_DESCRIPTOR_ARRAY_TYPE",
  154: "SOURCE_TEXT_MODULE_TYPE",
  155: "SYNTHETIC_MODULE_TYPE",
  156: "UNCOMPILED_DATA_WITH_PREPARSE_DATA_TYPE",
  157: "UNCOMPILED_DATA_WITHOUT_PREPARSE_DATA_TYPE",
  158: "WEAK_FIXED_ARRAY_TYPE",
  159: "TRANSITION_ARRAY_TYPE",
  160: "CELL_TYPE",
  161: "CODE_TYPE",
  162: "CODE_DATA_CONTAINER_TYPE",
  163: "COVERAGE_INFO_TYPE",
  164: "EMBEDDER_DATA_ARRAY_TYPE",
  165: "FEEDBACK_METADATA_TYPE",
  166: "FEEDBACK_VECTOR_TYPE",
  167: "FILLER_TYPE",
  168: "FREE_SPACE_TYPE",
  169: "INTERNAL_CLASS_TYPE",
  170: "INTERNAL_CLASS_WITH_STRUCT_ELEMENTS_TYPE",
  171: "MAP_TYPE",
  172: "ON_HEAP_BASIC_BLOCK_PROFILER_DATA_TYPE",
  173: "PREPARSE_DATA_TYPE",
  174: "PROPERTY_ARRAY_TYPE",
  175: "PROPERTY_CELL_TYPE",
  176: "SHARED_FUNCTION_INFO_TYPE",
  177: "SMI_BOX_TYPE",
  178: "SMI_PAIR_TYPE",
  179: "SORT_STATE_TYPE",
  180: "WASM_ARRAY_TYPE",
  181: "WASM_CAPI_FUNCTION_DATA_TYPE",
  182: "WASM_STRUCT_TYPE",
  183: "WEAK_ARRAY_LIST_TYPE",
  184: "WEAK_CELL_TYPE",
  185: "JS_PROXY_TYPE",
  1057: "JS_OBJECT_TYPE",
  186: "JS_GLOBAL_OBJECT_TYPE",
  187: "JS_GLOBAL_PROXY_TYPE",
  188: "JS_MODULE_NAMESPACE_TYPE",
  1040: "JS_SPECIAL_API_OBJECT_TYPE",
  1041: "JS_PRIMITIVE_WRAPPER_TYPE",
  1042: "JS_MAP_KEY_ITERATOR_TYPE",
  1043: "JS_MAP_KEY_VALUE_ITERATOR_TYPE",
  1044: "JS_MAP_VALUE_ITERATOR_TYPE",
  1045: "JS_SET_KEY_VALUE_ITERATOR_TYPE",
  1046: "JS_SET_VALUE_ITERATOR_TYPE",
  1047: "JS_GENERATOR_OBJECT_TYPE",
  1048: "JS_ASYNC_FUNCTION_OBJECT_TYPE",
  1049: "JS_ASYNC_GENERATOR_OBJECT_TYPE",
  1050: "JS_DATA_VIEW_TYPE",
  1051: "JS_TYPED_ARRAY_TYPE",
  1052: "JS_MAP_TYPE",
  1053: "JS_SET_TYPE",
  1054: "JS_WEAK_MAP_TYPE",
  1055: "JS_WEAK_SET_TYPE",
  1056: "JS_API_OBJECT_TYPE",
  1058: "JS_ARGUMENTS_OBJECT_TYPE",
  1059: "JS_ARRAY_TYPE",
  1060: "JS_ARRAY_BUFFER_TYPE",
  1061: "JS_ARRAY_ITERATOR_TYPE",
  1062: "JS_ASYNC_FROM_SYNC_ITERATOR_TYPE",
  1063: "JS_COLLATOR_TYPE",
  1064: "JS_CONTEXT_EXTENSION_OBJECT_TYPE",
  1065: "JS_DATE_TYPE",
  1066: "JS_DATE_TIME_FORMAT_TYPE",
  1067: "JS_DISPLAY_NAMES_TYPE",
  1068: "JS_ERROR_TYPE",
  1069: "JS_FINALIZATION_REGISTRY_TYPE",
  1070: "JS_LIST_FORMAT_TYPE",
  1071: "JS_LOCALE_TYPE",
  1072: "JS_MESSAGE_OBJECT_TYPE",
  1073: "JS_NUMBER_FORMAT_TYPE",
  1074: "JS_PLURAL_RULES_TYPE",
  1075: "JS_PROMISE_TYPE",
  1076: "JS_REG_EXP_TYPE",
  1077: "JS_REG_EXP_STRING_ITERATOR_TYPE",
  1078: "JS_RELATIVE_TIME_FORMAT_TYPE",
  1079: "JS_SEGMENT_ITERATOR_TYPE",
  1080: "JS_SEGMENTER_TYPE",
  1081: "JS_SEGMENTS_TYPE",
  1082: "JS_STRING_ITERATOR_TYPE",
  1083: "JS_V8_BREAK_ITERATOR_TYPE",
  1084: "JS_WEAK_REF_TYPE",
  1085: "WASM_EXCEPTION_OBJECT_TYPE",
  1086: "WASM_GLOBAL_OBJECT_TYPE",
  1087: "WASM_INSTANCE_OBJECT_TYPE",
  1088: "WASM_MEMORY_OBJECT_TYPE",
  1089: "WASM_MODULE_OBJECT_TYPE",
  1090: "WASM_TABLE_OBJECT_TYPE",
  1091: "JS_BOUND_FUNCTION_TYPE",
  1092: "JS_FUNCTION_TYPE",
}

# List of known V8 maps.
KNOWN_MAPS = {
  ("read_only_space", 0x02115): (171, "MetaMap"),
  ("read_only_space", 0x0213d): (67, "NullMap"),
  ("read_only_space", 0x02165): (153, "StrongDescriptorArrayMap"),
  ("read_only_space", 0x0218d): (158, "WeakFixedArrayMap"),
  ("read_only_space", 0x021cd): (96, "EnumCacheMap"),
  ("read_only_space", 0x02201): (117, "FixedArrayMap"),
  ("read_only_space", 0x0224d): (8, "OneByteInternalizedStringMap"),
  ("read_only_space", 0x02299): (168, "FreeSpaceMap"),
  ("read_only_space", 0x022c1): (167, "OnePointerFillerMap"),
  ("read_only_space", 0x022e9): (167, "TwoPointerFillerMap"),
  ("read_only_space", 0x02311): (67, "UninitializedMap"),
  ("read_only_space", 0x02389): (67, "UndefinedMap"),
  ("read_only_space", 0x023cd): (66, "HeapNumberMap"),
  ("read_only_space", 0x02401): (67, "TheHoleMap"),
  ("read_only_space", 0x02461): (67, "BooleanMap"),
  ("read_only_space", 0x02505): (131, "ByteArrayMap"),
  ("read_only_space", 0x0252d): (117, "FixedCOWArrayMap"),
  ("read_only_space", 0x02555): (118, "HashTableMap"),
  ("read_only_space", 0x0257d): (64, "SymbolMap"),
  ("read_only_space", 0x025a5): (40, "OneByteStringMap"),
  ("read_only_space", 0x025cd): (129, "ScopeInfoMap"),
  ("read_only_space", 0x025f5): (176, "SharedFunctionInfoMap"),
  ("read_only_space", 0x0261d): (161, "CodeMap"),
  ("read_only_space", 0x02645): (160, "CellMap"),
  ("read_only_space", 0x0266d): (175, "GlobalPropertyCellMap"),
  ("read_only_space", 0x02695): (70, "ForeignMap"),
  ("read_only_space", 0x026bd): (159, "TransitionArrayMap"),
  ("read_only_space", 0x026e5): (45, "ThinOneByteStringMap"),
  ("read_only_space", 0x0270d): (166, "FeedbackVectorMap"),
  ("read_only_space", 0x02749): (67, "ArgumentsMarkerMap"),
  ("read_only_space", 0x027a9): (67, "ExceptionMap"),
  ("read_only_space", 0x02805): (67, "TerminationExceptionMap"),
  ("read_only_space", 0x0286d): (67, "OptimizedOutMap"),
  ("read_only_space", 0x028cd): (67, "StaleRegisterMap"),
  ("read_only_space", 0x0292d): (130, "ScriptContextTableMap"),
  ("read_only_space", 0x02955): (127, "ClosureFeedbackCellArrayMap"),
  ("read_only_space", 0x0297d): (165, "FeedbackMetadataArrayMap"),
  ("read_only_space", 0x029a5): (117, "ArrayListMap"),
  ("read_only_space", 0x029cd): (65, "BigIntMap"),
  ("read_only_space", 0x029f5): (128, "ObjectBoilerplateDescriptionMap"),
  ("read_only_space", 0x02a1d): (132, "BytecodeArrayMap"),
  ("read_only_space", 0x02a45): (162, "CodeDataContainerMap"),
  ("read_only_space", 0x02a6d): (163, "CoverageInfoMap"),
  ("read_only_space", 0x02a95): (133, "FixedDoubleArrayMap"),
  ("read_only_space", 0x02abd): (120, "GlobalDictionaryMap"),
  ("read_only_space", 0x02ae5): (97, "ManyClosuresCellMap"),
  ("read_only_space", 0x02b0d): (117, "ModuleInfoMap"),
  ("read_only_space", 0x02b35): (121, "NameDictionaryMap"),
  ("read_only_space", 0x02b5d): (97, "NoClosuresCellMap"),
  ("read_only_space", 0x02b85): (122, "NumberDictionaryMap"),
  ("read_only_space", 0x02bad): (97, "OneClosureCellMap"),
  ("read_only_space", 0x02bd5): (123, "OrderedHashMapMap"),
  ("read_only_space", 0x02bfd): (124, "OrderedHashSetMap"),
  ("read_only_space", 0x02c25): (125, "OrderedNameDictionaryMap"),
  ("read_only_space", 0x02c4d): (173, "PreparseDataMap"),
  ("read_only_space", 0x02c75): (174, "PropertyArrayMap"),
  ("read_only_space", 0x02c9d): (93, "SideEffectCallHandlerInfoMap"),
  ("read_only_space", 0x02cc5): (93, "SideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02ced): (93, "NextCallSideEffectFreeCallHandlerInfoMap"),
  ("read_only_space", 0x02d15): (126, "SimpleNumberDictionaryMap"),
  ("read_only_space", 0x02d3d): (149, "SmallOrderedHashMapMap"),
  ("read_only_space", 0x02d65): (150, "SmallOrderedHashSetMap"),
  ("read_only_space", 0x02d8d): (151, "SmallOrderedNameDictionaryMap"),
  ("read_only_space", 0x02db5): (154, "SourceTextModuleMap"),
  ("read_only_space", 0x02ddd): (155, "SyntheticModuleMap"),
  ("read_only_space", 0x02e05): (71, "WasmTypeInfoMap"),
  ("read_only_space", 0x02e2d): (183, "WeakArrayListMap"),
  ("read_only_space", 0x02e55): (119, "EphemeronHashTableMap"),
  ("read_only_space", 0x02e7d): (164, "EmbedderDataArrayMap"),
  ("read_only_space", 0x02ea5): (184, "WeakCellMap"),
  ("read_only_space", 0x02ecd): (32, "StringMap"),
  ("read_only_space", 0x02ef5): (41, "ConsOneByteStringMap"),
  ("read_only_space", 0x02f1d): (33, "ConsStringMap"),
  ("read_only_space", 0x02f45): (37, "ThinStringMap"),
  ("read_only_space", 0x02f6d): (35, "SlicedStringMap"),
  ("read_only_space", 0x02f95): (43, "SlicedOneByteStringMap"),
  ("read_only_space", 0x02fbd): (34, "ExternalStringMap"),
  ("read_only_space", 0x02fe5): (42, "ExternalOneByteStringMap"),
  ("read_only_space", 0x0300d): (50, "UncachedExternalStringMap"),
  ("read_only_space", 0x03035): (0, "InternalizedStringMap"),
  ("read_only_space", 0x0305d): (2, "ExternalInternalizedStringMap"),
  ("read_only_space", 0x03085): (10, "ExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x030ad): (18, "UncachedExternalInternalizedStringMap"),
  ("read_only_space", 0x030d5): (26, "UncachedExternalOneByteInternalizedStringMap"),
  ("read_only_space", 0x030fd): (58, "UncachedExternalOneByteStringMap"),
  ("read_only_space", 0x03125): (67, "SelfReferenceMarkerMap"),
  ("read_only_space", 0x0314d): (67, "BasicBlockCountersMarkerMap"),
  ("read_only_space", 0x03191): (87, "ArrayBoilerplateDescriptionMap"),
  ("read_only_space", 0x03279): (99, "InterceptorInfoMap"),
  ("read_only_space", 0x053a5): (72, "PromiseFulfillReactionJobTaskMap"),
  ("read_only_space", 0x053cd): (73, "PromiseRejectReactionJobTaskMap"),
  ("read_only_space", 0x053f5): (74, "CallableTaskMap"),
  ("read_only_space", 0x0541d): (75, "CallbackTaskMap"),
  ("read_only_space", 0x05445): (76, "PromiseResolveThenableJobTaskMap"),
  ("read_only_space", 0x0546d): (79, "FunctionTemplateInfoMap"),
  ("read_only_space", 0x05495): (80, "ObjectTemplateInfoMap"),
  ("read_only_space", 0x054bd): (81, "AccessCheckInfoMap"),
  ("read_only_space", 0x054e5): (82, "AccessorInfoMap"),
  ("read_only_space", 0x0550d): (83, "AccessorPairMap"),
  ("read_only_space", 0x05535): (84, "AliasedArgumentsEntryMap"),
  ("read_only_space", 0x0555d): (85, "AllocationMementoMap"),
  ("read_only_space", 0x05585): (88, "AsmWasmDataMap"),
  ("read_only_space", 0x055ad): (89, "AsyncGeneratorRequestMap"),
  ("read_only_space", 0x055d5): (90, "BreakPointMap"),
  ("read_only_space", 0x055fd): (91, "BreakPointInfoMap"),
  ("read_only_space", 0x05625): (92, "CachedTemplateObjectMap"),
  ("read_only_space", 0x0564d): (94, "ClassPositionsMap"),
  ("read_only_space", 0x05675): (95, "DebugInfoMap"),
  ("read_only_space", 0x0569d): (98, "FunctionTemplateRareDataMap"),
  ("read_only_space", 0x056c5): (100, "InterpreterDataMap"),
  ("read_only_space", 0x056ed): (101, "ModuleRequestMap"),
  ("read_only_space", 0x05715): (102, "PromiseCapabilityMap"),
  ("read_only_space", 0x0573d): (103, "PromiseReactionMap"),
  ("read_only_space", 0x05765): (104, "PropertyDescriptorObjectMap"),
  ("read_only_space", 0x0578d): (105, "PrototypeInfoMap"),
  ("read_only_space", 0x057b5): (106, "ScriptMap"),
  ("read_only_space", 0x057dd): (107, "SourceTextModuleInfoEntryMap"),
  ("read_only_space", 0x05805): (108, "StackFrameInfoMap"),
  ("read_only_space", 0x0582d): (109, "StackTraceFrameMap"),
  ("read_only_space", 0x05855): (110, "TemplateObjectDescriptionMap"),
  ("read_only_space", 0x0587d): (111, "Tuple2Map"),
  ("read_only_space", 0x058a5): (112, "WasmExceptionTagMap"),
  ("read_only_space", 0x058cd): (113, "WasmExportedFunctionDataMap"),
  ("read_only_space", 0x058f5): (114, "WasmIndirectFunctionTableMap"),
  ("read_only_space", 0x0591d): (115, "WasmJSFunctionDataMap"),
  ("read_only_space", 0x05945): (116, "WasmValueMap"),
  ("read_only_space", 0x0596d): (135, "SloppyArgumentsElementsMap"),
  ("read_only_space", 0x05995): (152, "DescriptorArrayMap"),
  ("read_only_space", 0x059bd): (157, "UncompiledDataWithoutPreparseDataMap"),
  ("read_only_space", 0x059e5): (156, "UncompiledDataWithPreparseDataMap"),
  ("read_only_space", 0x05a0d): (172, "OnHeapBasicBlockProfilerDataMap"),
  ("read_only_space", 0x05a35): (181, "WasmCapiFunctionDataMap"),
  ("read_only_space", 0x05a5d): (169, "InternalClassMap"),
  ("read_only_space", 0x05a85): (178, "SmiPairMap"),
  ("read_only_space", 0x05aad): (177, "SmiBoxMap"),
  ("read_only_space", 0x05ad5): (146, "ExportedSubClassBaseMap"),
  ("read_only_space", 0x05afd): (147, "ExportedSubClassMap"),
  ("read_only_space", 0x05b25): (68, "AbstractInternalClassSubclass1Map"),
  ("read_only_space", 0x05b4d): (69, "AbstractInternalClassSubclass2Map"),
  ("read_only_space", 0x05b75): (134, "InternalClassWithSmiElementsMap"),
  ("read_only_space", 0x05b9d): (170, "InternalClassWithStructElementsMap"),
  ("read_only_space", 0x05bc5): (148, "ExportedSubClass2Map"),
  ("read_only_space", 0x05bed): (179, "SortStateMap"),
  ("read_only_space", 0x05c15): (86, "AllocationSiteWithWeakNextMap"),
  ("read_only_space", 0x05c3d): (86, "AllocationSiteWithoutWeakNextMap"),
  ("read_only_space", 0x05c65): (77, "LoadHandler1Map"),
  ("read_only_space", 0x05c8d): (77, "LoadHandler2Map"),
  ("read_only_space", 0x05cb5): (77, "LoadHandler3Map"),
  ("read_only_space", 0x05cdd): (78, "StoreHandler0Map"),
  ("read_only_space", 0x05d05): (78, "StoreHandler1Map"),
  ("read_only_space", 0x05d2d): (78, "StoreHandler2Map"),
  ("read_only_space", 0x05d55): (78, "StoreHandler3Map"),
  ("map_space", 0x02115): (1057, "ExternalMap"),
  ("map_space", 0x0213d): (1072, "JSMessageObjectMap"),
  ("map_space", 0x02165): (182, "WasmRttEqrefMap"),
  ("map_space", 0x0218d): (182, "WasmRttAnyrefMap"),
  ("map_space", 0x021b5): (182, "WasmRttExternrefMap"),
  ("map_space", 0x021dd): (182, "WasmRttFuncrefMap"),
  ("map_space", 0x02205): (182, "WasmRttI31refMap"),
}

# List of known V8 objects.
KNOWN_OBJECTS = {
  ("read_only_space", 0x021b5): "EmptyWeakFixedArray",
  ("read_only_space", 0x021bd): "EmptyDescriptorArray",
  ("read_only_space", 0x021f5): "EmptyEnumCache",
  ("read_only_space", 0x02229): "EmptyFixedArray",
  ("read_only_space", 0x02231): "NullValue",
  ("read_only_space", 0x02339): "UninitializedValue",
  ("read_only_space", 0x023b1): "UndefinedValue",
  ("read_only_space", 0x023f5): "NanValue",
  ("read_only_space", 0x02429): "TheHoleValue",
  ("read_only_space", 0x02455): "HoleNanValue",
  ("read_only_space", 0x02489): "TrueValue",
  ("read_only_space", 0x024c9): "FalseValue",
  ("read_only_space", 0x024f9): "empty_string",
  ("read_only_space", 0x02735): "EmptyScopeInfo",
  ("read_only_space", 0x02771): "ArgumentsMarker",
  ("read_only_space", 0x027d1): "Exception",
  ("read_only_space", 0x0282d): "TerminationException",
  ("read_only_space", 0x02895): "OptimizedOut",
  ("read_only_space", 0x028f5): "StaleRegister",
  ("read_only_space", 0x03175): "EmptyPropertyArray",
  ("read_only_space", 0x0317d): "EmptyByteArray",
  ("read_only_space", 0x03185): "EmptyObjectBoilerplateDescription",
  ("read_only_space", 0x031b9): "EmptyArrayBoilerplateDescription",
  ("read_only_space", 0x031c5): "EmptyClosureFeedbackCellArray",
  ("read_only_space", 0x031cd): "EmptySlowElementDictionary",
  ("read_only_space", 0x031f1): "EmptyOrderedHashMap",
  ("read_only_space", 0x03205): "EmptyOrderedHashSet",
  ("read_only_space", 0x03219): "EmptyFeedbackMetadata",
  ("read_only_space", 0x03225): "EmptyPropertyCell",
  ("read_only_space", 0x03239): "EmptyPropertyDictionary",
  ("read_only_space", 0x03261): "EmptyOrderedPropertyDictionary",
  ("read_only_space", 0x032a1): "NoOpInterceptorInfo",
  ("read_only_space", 0x032c9): "EmptyWeakArrayList",
  ("read_only_space", 0x032d5): "InfinityValue",
  ("read_only_space", 0x032e1): "MinusZeroValue",
  ("read_only_space", 0x032ed): "MinusInfinityValue",
  ("read_only_space", 0x032f9): "SelfReferenceMarker",
  ("read_only_space", 0x03339): "BasicBlockCountersMarker",
  ("read_only_space", 0x0337d): "OffHeapTrampolineRelocationInfo",
  ("read_only_space", 0x03389): "TrampolineTrivialCodeDataContainer",
  ("read_only_space", 0x03395): "TrampolinePromiseRejectionCodeDataContainer",
  ("read_only_space", 0x033a1): "GlobalThisBindingScopeInfo",
  ("read_only_space", 0x033d9): "EmptyFunctionScopeInfo",
  ("read_only_space", 0x03401): "NativeScopeInfo",
  ("read_only_space", 0x0341d): "HashSeed",
  ("old_space", 0x02115): "ArgumentsIteratorAccessor",
  ("old_space", 0x02159): "ArrayLengthAccessor",
  ("old_space", 0x0219d): "BoundFunctionLengthAccessor",
  ("old_space", 0x021e1): "BoundFunctionNameAccessor",
  ("old_space", 0x02225): "ErrorStackAccessor",
  ("old_space", 0x02269): "FunctionArgumentsAccessor",
  ("old_space", 0x022ad): "FunctionCallerAccessor",
  ("old_space", 0x022f1): "FunctionNameAccessor",
  ("old_space", 0x02335): "FunctionLengthAccessor",
  ("old_space", 0x02379): "FunctionPrototypeAccessor",
  ("old_space", 0x023bd): "RegExpResultIndicesAccessor",
  ("old_space", 0x02401): "StringLengthAccessor",
  ("old_space", 0x02445): "InvalidPrototypeValidityCell",
  ("old_space", 0x02531): "EmptyScript",
  ("old_space", 0x02571): "ManyClosuresCell",
  ("old_space", 0x0257d): "ArrayConstructorProtector",
  ("old_space", 0x02591): "NoElementsProtector",
  ("old_space", 0x025a5): "IsConcatSpreadableProtector",
  ("old_space", 0x025b9): "ArraySpeciesProtector",
  ("old_space", 0x025cd): "TypedArraySpeciesProtector",
  ("old_space", 0x025e1): "PromiseSpeciesProtector",
  ("old_space", 0x025f5): "RegExpSpeciesProtector",
  ("old_space", 0x02609): "StringLengthProtector",
  ("old_space", 0x0261d): "ArrayIteratorProtector",
  ("old_space", 0x02631): "ArrayBufferDetachingProtector",
  ("old_space", 0x02645): "PromiseHookProtector",
  ("old_space", 0x02659): "PromiseResolveProtector",
  ("old_space", 0x0266d): "MapIteratorProtector",
  ("old_space", 0x02681): "PromiseThenProtector",
  ("old_space", 0x02695): "SetIteratorProtector",
  ("old_space", 0x026a9): "StringIteratorProtector",
  ("old_space", 0x026bd): "SingleCharacterStringCache",
  ("old_space", 0x02ac5): "StringSplitCache",
  ("old_space", 0x02ecd): "RegExpMultipleCache",
  ("old_space", 0x032d5): "BuiltinsConstantsTable",
  ("old_space", 0x036bd): "AsyncFunctionAwaitRejectSharedFun",
  ("old_space", 0x036e1): "AsyncFunctionAwaitResolveSharedFun",
  ("old_space", 0x03705): "AsyncGeneratorAwaitRejectSharedFun",
  ("old_space", 0x03729): "AsyncGeneratorAwaitResolveSharedFun",
  ("old_space", 0x0374d): "AsyncGeneratorYieldResolveSharedFun",
  ("old_space", 0x03771): "AsyncGeneratorReturnResolveSharedFun",
  ("old_space", 0x03795): "AsyncGeneratorReturnClosedRejectSharedFun",
  ("old_space", 0x037b9): "AsyncGeneratorReturnClosedResolveSharedFun",
  ("old_space", 0x037dd): "AsyncIteratorValueUnwrapSharedFun",
  ("old_space", 0x03801): "PromiseAllResolveElementSharedFun",
  ("old_space", 0x03825): "PromiseAllSettledResolveElementSharedFun",
  ("old_space", 0x03849): "PromiseAllSettledRejectElementSharedFun",
  ("old_space", 0x0386d): "PromiseAnyRejectElementSharedFun",
  ("old_space", 0x03891): "PromiseCapabilityDefaultRejectSharedFun",
  ("old_space", 0x038b5): "PromiseCapabilityDefaultResolveSharedFun",
  ("old_space", 0x038d9): "PromiseCatchFinallySharedFun",
  ("old_space", 0x038fd): "PromiseGetCapabilitiesExecutorSharedFun",
  ("old_space", 0x03921): "PromiseThenFinallySharedFun",
  ("old_space", 0x03945): "PromiseThrowerFinallySharedFun",
  ("old_space", 0x03969): "PromiseValueThunkFinallySharedFun",
  ("old_space", 0x0398d): "ProxyRevokeSharedFun",
}

# Lower 32 bits of first page addresses for various heap spaces.
HEAP_FIRST_PAGES = {
  0x08100000: "old_space",
  0x08140000: "map_space",
  0x08040000: "read_only_space",
}

# List of known V8 Frame Markers.
FRAME_MARKERS = (
  "ENTRY",
  "CONSTRUCT_ENTRY",
  "EXIT",
  "OPTIMIZED",
  "WASM",
  "WASM_TO_JS",
  "JS_TO_WASM",
  "WASM_DEBUG_BREAK",
  "C_WASM_ENTRY",
  "WASM_EXIT",
  "WASM_COMPILE_LAZY",
  "INTERPRETED",
  "STUB",
  "BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION",
  "JAVA_SCRIPT_BUILTIN_CONTINUATION_WITH_CATCH",
  "INTERNAL",
  "CONSTRUCT",
  "ARGUMENTS_ADAPTOR",
  "BUILTIN",
  "BUILTIN_EXIT",
  "NATIVE",
)

# This set of constants is generated from a shipping build.
