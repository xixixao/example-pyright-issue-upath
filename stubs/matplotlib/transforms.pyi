from typing import Literal, Sequence

import numpy as np
from matplotlib._typing import *
from matplotlib.figure import Figure
from matplotlib.patches import Patch
from matplotlib.path import Path

DEBUG = ...

class TransformNode:
    INVALID_NON_AFFINE = ...
    INVALID_AFFINE = ...
    INVALID = ...
    is_affine = ...
    is_bbox = ...
    pass_through = ...
    def __init__(self, shorthand_name: str = ...) -> None: ...
    if DEBUG:
        def __str__(self) -> str: ...

    def __getstate__(self): ...
    def __setstate__(self, data_dict): ...
    def __copy__(self): ...
    def invalidate(self): ...
    def set_children(self, *children): ...
    def frozen(self): ...

class BboxBase(TransformNode):
    is_bbox = ...
    is_affine = ...
    if DEBUG: ...

    def frozen(self): ...
    def __array__(self, *args, **kwargs): ...
    @property
    def x0(self) -> float: ...
    @property
    def y0(self) -> float: ...
    @property
    def x1(self) -> float: ...
    @property
    def y1(self) -> float: ...
    @property
    def p0(self) -> tuple[float, float]: ...
    @property
    def p1(self) -> tuple[float, float]: ...
    @property
    def xmin(self) -> float: ...
    @property
    def ymin(self) -> float: ...
    @property
    def xmax(self) -> float: ...
    @property
    def ymax(self) -> float: ...
    @property
    def min(self) -> tuple[float, float]: ...
    @property
    def max(self) -> tuple[float, float]: ...
    @property
    def intervalx(self) -> tuple[float, float]: ...
    @property
    def intervaly(self) -> tuple[float, float]: ...
    @property
    def width(self) -> float: ...
    @property
    def height(self) -> float: ...
    @property
    def size(self) -> tuple[float, float]: ...
    @property
    def bounds(self) -> tuple[float, float, float, float]: ...
    @property
    def extents(self) -> tuple[float, float, float, float]: ...
    def get_points(self): ...
    def containsx(self, x) -> bool: ...
    def containsy(self, y) -> bool: ...
    def contains(self, x, y) -> bool: ...
    def overlaps(self, other: BboxBase) -> bool: ...
    def fully_containsx(self, x: float) -> bool: ...
    def fully_containsy(self, y: float) -> bool: ...
    def fully_contains(self, x: float, y: float) -> bool: ...
    def fully_overlaps(self, other: BboxBase) -> bool: ...
    def transformed(self, transform: Transform): ...
    coefs = ...
    def anchored(
        self,
        c: Sequence[float] | Literal["C", "SW", "S", "SE", "E", "NE", "N", "NW", "W"],
        container: Bbox = ...,
    ): ...
    def shrunk(self, mx: float, my: float) -> Bbox: ...
    def shrunk_to_aspect(self, box_aspect: float, container=..., fig_aspect: float = ...) -> Bbox: ...
    def splitx(self, *args) -> list[Bbox]: ...
    def splity(self, *args) -> list[Bbox]: ...
    def count_contains(self, vertices) -> int: ...
    def count_overlaps(self, bboxes: Sequence[Bbox]) -> int: ...
    def expanded(self, sw: float, sh: float) -> Bbox: ...
    def padded(self, p: float) -> Bbox: ...
    def translated(self, tx: float, ty: float) -> Bbox: ...
    def corners(
        self,
    ) -> tuple[
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
        tuple[float, float],
    ]: ...
    def rotated(self, radians: float) -> Bbox: ...
    @staticmethod
    def union(bboxes: Sequence[Bbox]) -> Bbox: ...
    @staticmethod
    def intersection(bbox1: Bbox, bbox2: Bbox) -> None | Bbox: ...

class Bbox(BboxBase):
    def __init__(self, points: np.ndarray, **kwargs) -> None: ...
    def invalidate(self): ...
    def frozen(self): ...
    @staticmethod
    def unit() -> Bbox: ...
    @staticmethod
    def null() -> Bbox: ...
    @staticmethod
    def from_bounds(x0: float, y0: float, width: float, height: float) -> Bbox: ...
    @staticmethod
    def from_extents(*args, minpos: float | None = ...): ...
    def __format__(self, fmt: str): ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def ignore(self, value: bool): ...
    def update_from_path(
        self,
        path: Path,
        ignore: bool | None = ...,
        updatex: bool = True,
        updatey: bool = True,
    ): ...
    def update_from_data_x(self, x: np.ndarray, ignore: bool | None = ...): ...
    def update_from_data_y(self, y: np.ndarray, ignore: bool | None = ...): ...
    def update_from_data_xy(
        self,
        xy: np.ndarray,
        ignore: bool | None = ...,
        updatex: bool = True,
        updatey: bool = True,
    ): ...
    @BboxBase.x0.setter
    def x0(self, val: float): ...
    @BboxBase.y0.setter
    def y0(self, val: float): ...
    @BboxBase.x1.setter
    def x1(self, val: float): ...
    @BboxBase.y1.setter
    def y1(self, val: float): ...
    @BboxBase.p0.setter
    def p0(self, val: float): ...
    @BboxBase.p1.setter
    def p1(self, val: float): ...
    @BboxBase.intervalx.setter
    def intervalx(self, interval): ...
    @BboxBase.intervaly.setter
    def intervaly(self, interval): ...
    @BboxBase.bounds.setter
    def bounds(self, bounds): ...
    @property
    def minpos(self) -> float: ...
    @property
    def minposx(self) -> float: ...
    @property
    def minposy(self) -> float: ...
    def get_points(self) -> tuple[tuple[float, float], tuple[float, float]]: ...
    def set_points(self, points) -> tuple[tuple[float, float], tuple[float, float]]: ...
    def set(self, other: Bbox): ...
    def mutated(self) -> bool: ...
    def mutatedx(self) -> bool: ...
    def mutatedy(self) -> bool: ...

class TransformedBbox(BboxBase):
    def __init__(self, bbox: Bbox, transform: Transform, **kwargs) -> None: ...
    def get_points(self): ...

class LockableBbox(BboxBase):
    def __init__(
        self, bbox: Bbox, x0: float | None = ..., y0: float | None = ..., x1: float | None = ..., y1: float | None = ..., **kwargs
    ) -> None: ...
    def get_points(self): ...
    @property
    def locked_x0(self) -> float | None: ...
    @locked_x0.setter
    def locked_x0(self, x0: float | None): ...
    @property
    def locked_y0(self) -> float | None: ...
    @locked_y0.setter
    def locked_y0(self, y0: float | None): ...
    @property
    def locked_x1(self) -> float | None: ...
    @locked_x1.setter
    def locked_x1(self, x1: float | None): ...
    @property
    def locked_y1(self) -> float | None: ...
    @locked_y1.setter
    def locked_y1(self, y1: float | None): ...

class Transform(TransformNode):
    input_dims = ...
    output_dims = ...
    is_separable = ...
    has_inverse = ...
    def __init_subclass__(cls): ...
    def __add__(self, other: Transform) -> Transform: ...
    @property
    def depth(self) -> int: ...
    def contains_branch(self, other: Transform): ...
    def contains_branch_seperately(self, other_transform: Transform): ...
    def __sub__(self, other: Transform) -> Transform: ...
    def __array__(self, *args, **kwargs): ...
    def transform(self, values: ArrayLike) -> np.ndarray: ...
    def transform_affine(self, values: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, values: ArrayLike) -> np.ndarray: ...
    def transform_bbox(self, bbox: Bbox): ...
    def get_affine(self): ...
    def get_matrix(self): ...
    def transform_point(self, point): ...
    def transform_path(self, path: Path) -> Path: ...
    def transform_path_affine(self, path: Path) -> Path: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def transform_angles(
        self,
        angles: ArrayLike,
        pts: ArrayLike,
        radians: bool = ...,
        pushoff: float = ...,
    ) -> np.ndarray: ...
    def inverted(self) -> Transform: ...

class TransformWrapper(Transform):
    pass_through = ...
    def __init__(self, child: Transform) -> None: ...
    def __eq__(self, other: Transform) -> bool: ...
    def frozen(self): ...
    def set(self, child: Transform): ...
    is_affine = ...
    is_separable = ...
    has_inverse = ...

class AffineBase(Transform):
    is_affine = ...
    def __init__(self, *args, **kwargs) -> None: ...
    def __array__(self, *args, **kwargs): ...
    def __eq__(self, other) -> bool: ...
    def transform(self, values: ArrayLike) -> np.ndarray: ...
    def transform_affine(self, values: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path(self, path: Path) -> Path: ...
    def transform_path_affine(self, path: Path) -> Path: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...

class Affine2DBase(AffineBase):
    input_dims = ...
    output_dims = ...
    def frozen(self): ...
    @property
    def is_separable(self) -> bool: ...
    def to_values(self) -> tuple[float, float, float, float, float, float]: ...
    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def inverted(self) -> Transform: ...

class Affine2D(Affine2DBase):
    def __init__(self, matrix: ArrayLike = ..., **kwargs) -> None: ...
    def __str__(self) -> str: ...
    @staticmethod
    def from_values(a: float, b: float, c: float, d: float, e: float, f: float): ...
    def get_matrix(self) -> np.ndarray: ...
    def set_matrix(self, mtx: np.ndarray): ...
    def set(self, other: Transform): ...
    @staticmethod
    def identity() -> Affine2D: ...
    def clear(self) -> None: ...
    def rotate(self, theta: float) -> Affine2D: ...
    def rotate_deg(self, degrees: float) -> Affine2D: ...
    def rotate_around(self, x: float, y: float, theta: float) -> Affine2D: ...
    def rotate_deg_around(self, x: float, y: float, degrees: float) -> Affine2D: ...
    def translate(self, tx: float, ty: float) -> Affine2D: ...
    def scale(self, sx: float, sy: float = ...) -> Affine2D: ...
    def skew(self, xShear: float, yShear: float) -> Affine2D: ...
    def skew_deg(self, xShear: float, yShear: float) -> Affine2D: ...

class IdentityTransform(Affine2DBase):
    _mtx = np.identity(3)
    def frozen(self): ...
    def get_matrix(self): ...
    def transform(self, points: ArrayLike) -> np.ndarray: ...
    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path(self, path: Path) -> Path: ...
    def transform_path_affine(self, path: Path) -> Path: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...
    def inverted(self) -> Transform: ...

class _BlendedMixin:
    def __eq__(self, other) -> bool: ...
    def contains_branch_seperately(self, transform: Transform) -> bool: ...

class BlendedGenericTransform(_BlendedMixin, Transform):
    input_dims = ...
    output_dims = ...
    is_separable = ...
    pass_through = ...
    def __init__(self, x_transform: Transform, y_transform: Transform, **kwargs) -> None: ...
    @property
    def depth(self): ...
    def contains_branch(self, other: Transform) -> bool: ...

    is_affine = ...
    has_inverse = ...
    def frozen(self): ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def inverted(self) -> Transform: ...
    def get_affine(self): ...

class BlendedAffine2D(_BlendedMixin, Affine2DBase):
    is_separable = ...
    def __init__(self, x_transform: Transform, y_transform: Transform, **kwargs) -> None: ...
    def get_matrix(self): ...

def blended_transform_factory(x_transform: Transform, y_transform: Transform) -> Transform: ...

class CompositeGenericTransform(Transform):
    pass_through = ...
    def __init__(self, a: Transform, b: Transform, **kwargs) -> None: ...
    def frozen(self): ...
    def __eq__(self, other) -> bool: ...

    depth = ...
    is_affine = ...
    is_separable = ...
    has_inverse = ...

    def transform_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_non_affine(self, points: ArrayLike) -> np.ndarray: ...
    def transform_path_non_affine(self, path: Path) -> Path: ...
    def get_affine(self): ...
    def inverted(self) -> Transform: ...

class CompositeAffine2D(Affine2DBase):
    def __init__(self, a: Transform, b: Transform, **kwargs) -> None: ...
    @property
    def depth(self): ...
    def get_matrix(self): ...

def composite_transform_factory(a: Transform, b: Transform) -> Transform: ...

class BboxTransform(Affine2DBase):
    is_separable = ...
    def __init__(self, boxin, boxout, **kwargs) -> None: ...
    def get_matrix(self): ...

class BboxTransformTo(Affine2DBase):
    is_separable = ...
    def __init__(self, boxout, **kwargs) -> None: ...
    def get_matrix(self): ...

class BboxTransformToMaxOnly(BboxTransformTo):
    def get_matrix(self): ...

class BboxTransformFrom(Affine2DBase):
    is_separable = ...
    def __init__(self, boxin, **kwargs) -> None: ...
    def get_matrix(self): ...

class ScaledTranslation(Affine2DBase):
    def __init__(self, xt: float, yt: float, scale_trans, **kwargs) -> None: ...
    def get_matrix(self): ...

class AffineDeltaTransform(Affine2DBase):
    def __init__(self, transform: Transform, **kwargs) -> None: ...
    def get_matrix(self): ...

class TransformedPath(TransformNode):
    def __init__(self, path, transform: Transform) -> None: ...
    def get_transformed_points_and_affine(self) -> Path: ...
    def get_transformed_path_and_affine(self) -> Path: ...
    def get_fully_transformed_path(self) -> Path: ...
    def get_affine(self): ...

class TransformedPatchPath(TransformedPath):
    def __init__(self, patch: Patch) -> None: ...

def nonsingular(
    vmin: float,
    vmax: float,
    expander: float = ...,
    tiny: float = ...,
    increasing: bool = ...,
): ...
def interval_contains(interval: Sequence[float], val: float) -> bool: ...
def interval_contains_open(interval: Sequence[float], val: float) -> bool: ...
def offset_copy(
    trans: Transform,
    fig: Figure | None = None,
    x: float = 0,
    y: float = 0,
    units: Literal["inches", "points", "dots"] = "inches",
) -> Transform: ...
