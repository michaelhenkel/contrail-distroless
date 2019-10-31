
# AUTO-GENERATED file from IFMapApiGenerator. Do Not Edit!

from contrail_heat.resources import contrail
try:
    from heat.common.i18n import _
except ImportError:
    pass
from heat.engine import attributes
from heat.engine import constraints
from heat.engine import properties
try:
    from heat.openstack.common import log as logging
except ImportError:
    from oslo_log import log as logging
import uuid

from vnc_api import vnc_api

LOG = logging.getLogger(__name__)


class ContrailSecurityLoggingObject(contrail.ContrailResource):
    PROPERTIES = (
        NAME, FQ_NAME, SECURITY_LOGGING_OBJECT_RULES, SECURITY_LOGGING_OBJECT_RULES_RULE, SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID, SECURITY_LOGGING_OBJECT_RULES_RULE_RATE, DISPLAY_NAME, PERMS2, PERMS2_OWNER, PERMS2_OWNER_ACCESS, PERMS2_GLOBAL_ACCESS, PERMS2_SHARE, PERMS2_SHARE_TENANT, PERMS2_SHARE_TENANT_ACCESS, SECURITY_LOGGING_OBJECT_RATE, ANNOTATIONS, ANNOTATIONS_KEY_VALUE_PAIR, ANNOTATIONS_KEY_VALUE_PAIR_KEY, ANNOTATIONS_KEY_VALUE_PAIR_VALUE, SECURITY_GROUP_REFS, SECURITY_GROUP_REFS_DATA, SECURITY_GROUP_REFS_DATA_RULE, SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID, SECURITY_GROUP_REFS_DATA_RULE_RATE, TAG_REFS, NETWORK_POLICY_REFS, NETWORK_POLICY_REFS_DATA, NETWORK_POLICY_REFS_DATA_RULE, NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID, NETWORK_POLICY_REFS_DATA_RULE_RATE, GLOBAL_VROUTER_CONFIG, PROJECT
    ) = (
        'name', 'fq_name', 'security_logging_object_rules', 'security_logging_object_rules_rule', 'security_logging_object_rules_rule_rule_uuid', 'security_logging_object_rules_rule_rate', 'display_name', 'perms2', 'perms2_owner', 'perms2_owner_access', 'perms2_global_access', 'perms2_share', 'perms2_share_tenant', 'perms2_share_tenant_access', 'security_logging_object_rate', 'annotations', 'annotations_key_value_pair', 'annotations_key_value_pair_key', 'annotations_key_value_pair_value', 'security_group_refs', 'security_group_refs_data', 'security_group_refs_data_rule', 'security_group_refs_data_rule_rule_uuid', 'security_group_refs_data_rule_rate', 'tag_refs', 'network_policy_refs', 'network_policy_refs_data', 'network_policy_refs_data_rule', 'network_policy_refs_data_rule_rule_uuid', 'network_policy_refs_data_rule_rate', 'global_vrouter_config', 'project'
    )

    properties_schema = {
        NAME: properties.Schema(
            properties.Schema.STRING,
            _('NAME.'),
            update_allowed=True,
            required=False,
        ),
        FQ_NAME: properties.Schema(
            properties.Schema.STRING,
            _('FQ_NAME.'),
            update_allowed=True,
            required=False,
        ),
        SECURITY_LOGGING_OBJECT_RULES: properties.Schema(
            properties.Schema.MAP,
            _('SECURITY_LOGGING_OBJECT_RULES.'),
            update_allowed=True,
            required=False,
            schema={
                SECURITY_LOGGING_OBJECT_RULES_RULE: properties.Schema(
                    properties.Schema.LIST,
                    _('SECURITY_LOGGING_OBJECT_RULES_RULE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID: properties.Schema(
                                properties.Schema.STRING,
                                _('SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID.'),
                                update_allowed=True,
                                required=False,
                            ),
                            SECURITY_LOGGING_OBJECT_RULES_RULE_RATE: properties.Schema(
                                properties.Schema.INTEGER,
                                _('SECURITY_LOGGING_OBJECT_RULES_RULE_RATE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        DISPLAY_NAME: properties.Schema(
            properties.Schema.STRING,
            _('DISPLAY_NAME.'),
            update_allowed=True,
            required=False,
        ),
        PERMS2: properties.Schema(
            properties.Schema.MAP,
            _('PERMS2.'),
            update_allowed=True,
            required=False,
            schema={
                PERMS2_OWNER: properties.Schema(
                    properties.Schema.STRING,
                    _('PERMS2_OWNER.'),
                    update_allowed=True,
                    required=False,
                ),
                PERMS2_OWNER_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_OWNER_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_GLOBAL_ACCESS: properties.Schema(
                    properties.Schema.INTEGER,
                    _('PERMS2_GLOBAL_ACCESS.'),
                    update_allowed=True,
                    required=False,
                    constraints=[
                        constraints.Range(0, 7),
                    ],
                ),
                PERMS2_SHARE: properties.Schema(
                    properties.Schema.LIST,
                    _('PERMS2_SHARE.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            PERMS2_SHARE_TENANT: properties.Schema(
                                properties.Schema.STRING,
                                _('PERMS2_SHARE_TENANT.'),
                                update_allowed=True,
                                required=False,
                            ),
                            PERMS2_SHARE_TENANT_ACCESS: properties.Schema(
                                properties.Schema.INTEGER,
                                _('PERMS2_SHARE_TENANT_ACCESS.'),
                                update_allowed=True,
                                required=False,
                                constraints=[
                                    constraints.Range(0, 7),
                                ],
                            ),
                        }
                    )
                ),
            }
        ),
        SECURITY_LOGGING_OBJECT_RATE: properties.Schema(
            properties.Schema.INTEGER,
            _('SECURITY_LOGGING_OBJECT_RATE.'),
            update_allowed=True,
            required=False,
        ),
        ANNOTATIONS: properties.Schema(
            properties.Schema.MAP,
            _('ANNOTATIONS.'),
            update_allowed=True,
            required=False,
            schema={
                ANNOTATIONS_KEY_VALUE_PAIR: properties.Schema(
                    properties.Schema.LIST,
                    _('ANNOTATIONS_KEY_VALUE_PAIR.'),
                    update_allowed=True,
                    required=False,
                    schema=properties.Schema(
                        properties.Schema.MAP,
                        schema={
                            ANNOTATIONS_KEY_VALUE_PAIR_KEY: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_KEY.'),
                                update_allowed=True,
                                required=False,
                            ),
                            ANNOTATIONS_KEY_VALUE_PAIR_VALUE: properties.Schema(
                                properties.Schema.STRING,
                                _('ANNOTATIONS_KEY_VALUE_PAIR_VALUE.'),
                                update_allowed=True,
                                required=False,
                            ),
                        }
                    )
                ),
            }
        ),
        SECURITY_GROUP_REFS: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_GROUP_REFS.'),
            update_allowed=True,
            required=False,
        ),
        SECURITY_GROUP_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('SECURITY_GROUP_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    SECURITY_GROUP_REFS_DATA_RULE: properties.Schema(
                        properties.Schema.LIST,
                        _('SECURITY_GROUP_REFS_DATA_RULE.'),
                        update_allowed=True,
                        required=False,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID: properties.Schema(
                                    properties.Schema.STRING,
                                    _('SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                SECURITY_GROUP_REFS_DATA_RULE_RATE: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('SECURITY_GROUP_REFS_DATA_RULE_RATE.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        )
                    ),
                }
            )
        ),
        TAG_REFS: properties.Schema(
            properties.Schema.LIST,
            _('TAG_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS.'),
            update_allowed=True,
            required=False,
        ),
        NETWORK_POLICY_REFS_DATA: properties.Schema(
            properties.Schema.LIST,
            _('NETWORK_POLICY_REFS_DATA.'),
            update_allowed=True,
            required=False,
            schema=properties.Schema(
                properties.Schema.MAP,
                schema={
                    NETWORK_POLICY_REFS_DATA_RULE: properties.Schema(
                        properties.Schema.LIST,
                        _('NETWORK_POLICY_REFS_DATA_RULE.'),
                        update_allowed=True,
                        required=False,
                        schema=properties.Schema(
                            properties.Schema.MAP,
                            schema={
                                NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID: properties.Schema(
                                    properties.Schema.STRING,
                                    _('NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                                NETWORK_POLICY_REFS_DATA_RULE_RATE: properties.Schema(
                                    properties.Schema.INTEGER,
                                    _('NETWORK_POLICY_REFS_DATA_RULE_RATE.'),
                                    update_allowed=True,
                                    required=False,
                                ),
                            }
                        )
                    ),
                }
            )
        ),
        GLOBAL_VROUTER_CONFIG: properties.Schema(
            properties.Schema.STRING,
            _('GLOBAL_VROUTER_CONFIG.'),
            update_allowed=True,
            required=False,
        ),
        PROJECT: properties.Schema(
            properties.Schema.STRING,
            _('PROJECT.'),
            update_allowed=True,
            required=False,
        ),
    }

    attributes_schema = {
        NAME: attributes.Schema(
            _('NAME.'),
        ),
        FQ_NAME: attributes.Schema(
            _('FQ_NAME.'),
        ),
        SECURITY_LOGGING_OBJECT_RULES: attributes.Schema(
            _('SECURITY_LOGGING_OBJECT_RULES.'),
        ),
        DISPLAY_NAME: attributes.Schema(
            _('DISPLAY_NAME.'),
        ),
        PERMS2: attributes.Schema(
            _('PERMS2.'),
        ),
        SECURITY_LOGGING_OBJECT_RATE: attributes.Schema(
            _('SECURITY_LOGGING_OBJECT_RATE.'),
        ),
        ANNOTATIONS: attributes.Schema(
            _('ANNOTATIONS.'),
        ),
        SECURITY_GROUP_REFS: attributes.Schema(
            _('SECURITY_GROUP_REFS.'),
        ),
        SECURITY_GROUP_REFS_DATA: attributes.Schema(
            _('SECURITY_GROUP_REFS_DATA.'),
        ),
        TAG_REFS: attributes.Schema(
            _('TAG_REFS.'),
        ),
        NETWORK_POLICY_REFS: attributes.Schema(
            _('NETWORK_POLICY_REFS.'),
        ),
        NETWORK_POLICY_REFS_DATA: attributes.Schema(
            _('NETWORK_POLICY_REFS_DATA.'),
        ),
        GLOBAL_VROUTER_CONFIG: attributes.Schema(
            _('GLOBAL_VROUTER_CONFIG.'),
        ),
        PROJECT: attributes.Schema(
            _('PROJECT.'),
        ),
    }

    update_allowed_keys = ('Properties',)

    @contrail.set_auth_token
    def handle_create(self):
        parent_obj = None
        if parent_obj is None and self.properties.get(self.GLOBAL_VROUTER_CONFIG) and self.properties.get(self.GLOBAL_VROUTER_CONFIG) != 'config-root':
            try:
                parent_obj = self.vnc_lib().global_vrouter_config_read(fq_name_str=self.properties.get(self.GLOBAL_VROUTER_CONFIG))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().global_vrouter_config_read(id=str(uuid.UUID(self.properties.get(self.GLOBAL_VROUTER_CONFIG))))
            except:
                parent_obj = None
        if parent_obj is None and self.properties.get(self.PROJECT) and self.properties.get(self.PROJECT) != 'config-root':
            try:
                parent_obj = self.vnc_lib().project_read(fq_name_str=self.properties.get(self.PROJECT))
            except vnc_api.NoIdError:
                parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(self.properties.get(self.PROJECT))))
            except:
                parent_obj = None

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            tenant_id = self.stack.context.tenant_id
            parent_obj = self.vnc_lib().project_read(id=str(uuid.UUID(tenant_id)))

        if parent_obj is None and self.properties.get(self.PROJECT) != 'config-root':
            raise Exception('Error: parent is not specified in template!')

        obj_0 = vnc_api.SecurityLoggingObject(name=self.properties[self.NAME],
            parent_obj=parent_obj)

        if self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES) is not None:
            obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
            if self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE) is not None:
                for index_1 in range(len(self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE))):
                    obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                    if self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID))
                    if self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RATE) is not None:
                        obj_2.set_rate(self.properties.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RATE))
                    obj_1.add_rule(obj_2)
            obj_0.set_security_logging_object_rules(obj_1)
        if self.properties.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(self.properties.get(self.DISPLAY_NAME))
        if self.properties.get(self.PERMS2) is not None:
            obj_1 = vnc_api.PermType2()
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER) is not None:
                obj_1.set_owner(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS) is not None:
                obj_1.set_owner_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_OWNER_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS) is not None:
                obj_1.set_global_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_GLOBAL_ACCESS))
            if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE) is not None:
                for index_1 in range(len(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE))):
                    obj_2 = vnc_api.ShareType()
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT) is not None:
                        obj_2.set_tenant(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT))
                    if self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS) is not None:
                        obj_2.set_tenant_access(self.properties.get(self.PERMS2, {}).get(self.PERMS2_SHARE, {})[index_1].get(self.PERMS2_SHARE_TENANT_ACCESS))
                    obj_1.add_share(obj_2)
            obj_0.set_perms2(obj_1)
        if self.properties.get(self.SECURITY_LOGGING_OBJECT_RATE) is not None:
            obj_0.set_security_logging_object_rate(self.properties.get(self.SECURITY_LOGGING_OBJECT_RATE))
        if self.properties.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(self.properties.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)

        # reference to security_group_refs
        if len(self.properties.get(self.SECURITY_GROUP_REFS) or []) != len(self.properties.get(self.SECURITY_GROUP_REFS_DATA) or []):
            raise Exception(_('security-logging-object: specify security_group_refs for each security_group_refs_data.'))
        obj_1 = None
        if self.properties.get(self.SECURITY_GROUP_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.SECURITY_GROUP_REFS_DATA))):
                obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
                if self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE) is not None:
                    for index_1 in range(len(self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE))):
                        obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                        if self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID) is not None:
                            obj_2.set_rule_uuid(self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID))
                        if self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RATE) is not None:
                            obj_2.set_rate(self.properties.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RATE))
                        obj_1.add_rule(obj_2)

                if self.properties.get(self.SECURITY_GROUP_REFS):
                    try:
                        ref_obj = self.vnc_lib().security_group_read(
                            id=self.properties.get(self.SECURITY_GROUP_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().security_group_read(
                            fq_name_str=self.properties.get(self.SECURITY_GROUP_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_security_group(ref_obj, obj_1)

        # reference to tag_refs
        if self.properties.get(self.TAG_REFS):
            for index_0 in range(len(self.properties.get(self.TAG_REFS))):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=self.properties.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                obj_0.add_tag(ref_obj)

        # reference to network_policy_refs
        if len(self.properties.get(self.NETWORK_POLICY_REFS) or []) != len(self.properties.get(self.NETWORK_POLICY_REFS_DATA) or []):
            raise Exception(_('security-logging-object: specify network_policy_refs for each network_policy_refs_data.'))
        obj_1 = None
        if self.properties.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(self.properties.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
                if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE) is not None:
                    for index_1 in range(len(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE))):
                        obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                        if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID) is not None:
                            obj_2.set_rule_uuid(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID))
                        if self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RATE) is not None:
                            obj_2.set_rate(self.properties.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RATE))
                        obj_1.add_rule(obj_2)

                if self.properties.get(self.NETWORK_POLICY_REFS):
                    try:
                        ref_obj = self.vnc_lib().network_policy_read(
                            id=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    except vnc_api.NoIdError:
                        ref_obj = self.vnc_lib().network_policy_read(
                            fq_name_str=self.properties.get(self.NETWORK_POLICY_REFS)[index_0]
                        )
                    except Exception as e:
                        raise Exception(_('%s') % str(e))
                    obj_0.add_network_policy(ref_obj, obj_1)

        try:
            obj_uuid = super(ContrailSecurityLoggingObject, self).resource_create(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

        self.resource_id_set(obj_uuid)

    @contrail.set_auth_token
    def handle_update(self, json_snippet, tmpl_diff, prop_diff):
        try:
            obj_0 = self.vnc_lib().security_logging_object_read(
                id=self.resource_id
            )
        except Exception as e:
            raise Exception(_('%s') % str(e))

        if prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES) is not None:
            obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
            if prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE) is not None:
                for index_1 in range(len(prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE))):
                    obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                    if prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID) is not None:
                        obj_2.set_rule_uuid(prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RULE_UUID))
                    if prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RATE) is not None:
                        obj_2.set_rate(prop_diff.get(self.SECURITY_LOGGING_OBJECT_RULES, {}).get(self.SECURITY_LOGGING_OBJECT_RULES_RULE, {})[index_1].get(self.SECURITY_LOGGING_OBJECT_RULES_RULE_RATE))
                    obj_1.add_rule(obj_2)
            obj_0.set_security_logging_object_rules(obj_1)
        if prop_diff.get(self.DISPLAY_NAME) is not None:
            obj_0.set_display_name(prop_diff.get(self.DISPLAY_NAME))
        if prop_diff.get(self.SECURITY_LOGGING_OBJECT_RATE) is not None:
            obj_0.set_security_logging_object_rate(prop_diff.get(self.SECURITY_LOGGING_OBJECT_RATE))
        if prop_diff.get(self.ANNOTATIONS) is not None:
            obj_1 = vnc_api.KeyValuePairs()
            if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR) is not None:
                for index_1 in range(len(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR))):
                    obj_2 = vnc_api.KeyValuePair()
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY) is not None:
                        obj_2.set_key(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_KEY))
                    if prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE) is not None:
                        obj_2.set_value(prop_diff.get(self.ANNOTATIONS, {}).get(self.ANNOTATIONS_KEY_VALUE_PAIR, {})[index_1].get(self.ANNOTATIONS_KEY_VALUE_PAIR_VALUE))
                    obj_1.add_key_value_pair(obj_2)
            obj_0.set_annotations(obj_1)

        # reference to security_group
        update = 0
        if not self.SECURITY_GROUP_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_security_group_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.SECURITY_GROUP_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_security_group_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.SECURITY_GROUP_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.SECURITY_GROUP_REFS_DATA))):
                obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
                if prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE) is not None:
                    for index_1 in range(len(prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE))):
                        obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                        if prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID) is not None:
                            obj_2.set_rule_uuid(prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RULE_UUID))
                        if prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RATE) is not None:
                            obj_2.set_rate(prop_diff.get(self.SECURITY_GROUP_REFS_DATA, {})[index_0].get(self.SECURITY_GROUP_REFS_DATA_RULE, {})[index_1].get(self.SECURITY_GROUP_REFS_DATA_RULE_RATE))
                        obj_1.add_rule(obj_2)
                ref_data_list.append(obj_1)
        if self.SECURITY_GROUP_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.SECURITY_GROUP_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().security_group_read(
                        id=prop_diff.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().security_group_read(
                        fq_name_str=prop_diff.get(self.SECURITY_GROUP_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('security-logging-object: specify security_group_refs_data for each security_group_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_security_group_list(ref_obj_list, ref_data_list)
        # End: reference to security_group_refs

        # reference to tag_refs
        ref_obj_list = []
        if self.TAG_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.TAG_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().tag_read(
                        id=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().tag_read(
                        fq_name_str=prop_diff.get(self.TAG_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append({'to':ref_obj.fq_name})

            obj_0.set_tag_list(ref_obj_list)
            # End: reference to tag_refs

        # reference to network_policy
        update = 0
        if not self.NETWORK_POLICY_REFS in prop_diff:
            ref_obj_list = [ref['to'] for ref in obj_0.get_network_policy_refs() or []]
        else:
            ref_obj_list = []
            update = 1
        if not self.NETWORK_POLICY_REFS_DATA in prop_diff:
            ref_data_list = [ref['attr'] for ref in obj_0.get_network_policy_refs() or []]
        else:
            ref_data_list = []

        if prop_diff.get(self.NETWORK_POLICY_REFS_DATA) is not None:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS_DATA))):
                obj_1 = vnc_api.SecurityLoggingObjectRuleListType()
                if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE) is not None:
                    for index_1 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE))):
                        obj_2 = vnc_api.SecurityLoggingObjectRuleEntryType()
                        if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID) is not None:
                            obj_2.set_rule_uuid(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RULE_UUID))
                        if prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RATE) is not None:
                            obj_2.set_rate(prop_diff.get(self.NETWORK_POLICY_REFS_DATA, {})[index_0].get(self.NETWORK_POLICY_REFS_DATA_RULE, {})[index_1].get(self.NETWORK_POLICY_REFS_DATA_RULE_RATE))
                        obj_1.add_rule(obj_2)
                ref_data_list.append(obj_1)
        if self.NETWORK_POLICY_REFS in prop_diff:
            for index_0 in range(len(prop_diff.get(self.NETWORK_POLICY_REFS) or [])):
                try:
                    ref_obj = self.vnc_lib().network_policy_read(
                        id=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                except vnc_api.NoIdError:
                    ref_obj = self.vnc_lib().network_policy_read(
                        fq_name_str=prop_diff.get(self.NETWORK_POLICY_REFS)[index_0]
                    )
                except Exception as e:
                    raise Exception(_('%s') % str(e))
                ref_obj_list.append(ref_obj.fq_name)

        if len(ref_obj_list) != len(ref_data_list):
            raise Exception(_('security-logging-object: specify network_policy_refs_data for each network_policy_refs.'))

        if update or ref_obj_list or ref_data_list:
            obj_0.set_network_policy_list(ref_obj_list, ref_data_list)
        # End: reference to network_policy_refs

        try:
            self.vnc_lib().security_logging_object_update(obj_0)
        except Exception as e:
            raise Exception(_('%s') % str(e))

    @contrail.set_auth_token
    def handle_delete(self):
        if self.resource_id is None:
            return

        try:
            self.vnc_lib().security_logging_object_delete(id=self.resource_id)
        except Exception as ex:
            self._ignore_not_found(ex)
            LOG.warn(_('security_logging_object %s already deleted.') % self.name)

    @contrail.set_auth_token
    def _show_resource(self):
        obj = self.vnc_lib().security_logging_object_read(id=self.resource_id)
        obj_dict = obj.serialize_to_json()
        return obj_dict


def resource_mapping():
    return {
        'OS::ContrailV2::SecurityLoggingObject': ContrailSecurityLoggingObject,
    }