import {
  ElementType,
  ReactNode,
  ComponentPropsWithoutRef,
  ReactElement,
  forwardRef,
  Ref,
} from "react";

/*
  forwardRefWithAs lets us forward refs while keeping the correct component type,
  which can be specified by the `as` prop.
*/

export type ElementTagNameMap = HTMLElementTagNameMap &
  Pick<
    SVGElementTagNameMap,
    Exclude<keyof SVGElementTagNameMap, keyof HTMLElementTagNameMap>
  >;

export type AsProp<Comp extends ElementType, Props> = {
  as?: Comp;
  ref?: Ref<
    Comp extends keyof ElementTagNameMap
      ? ElementTagNameMap[Comp]
      : Comp extends new (...args: any) => any
      ? InstanceType<Comp>
      : undefined
  >;
} & Omit<ComponentPropsWithoutRef<Comp>, "as" | keyof Props>;

export type CompWithAsProp<Props, DefaultElementType extends ElementType> = <
  Comp extends ElementType = DefaultElementType
>(
  props: AsProp<Comp, Props> & Props
) => ReactElement;

export const forwardRefWithAs = <
  DefaultElementType extends ElementType,
  BaseProps
>(
  render: (
    props: BaseProps & { as?: ElementType },
    ref: React.Ref<any>
  ) => Exclude<ReactNode, undefined>
): CompWithAsProp<BaseProps, DefaultElementType> => {
  // @ts-expect-error xxx
  return forwardRef(render);
};
